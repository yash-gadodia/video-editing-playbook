// Convert an HDR (HLG / PQ, BT.2020) camera file to an SDR BT.709 master using AVFoundation,
// so the rest of the pipeline can stay in ffmpeg without touching colour maths.
//
//   swift tosdr.swift input.MOV output.mov
//
// Why this exists: modern phones record HDR by default. Feeding that straight into ffmpeg
// gives you either a washed-out image (tags ignored) or, if you hand-roll an HLG->BT.709
// LUT, an orange over-saturated one (double system gamma + an over-wide primaries matrix).
// The usual zscale/tonemap recipe needs an ffmpeg built with libzimg, which many are not.
// Delegating to the OS tone mapper sidesteps all of it and matches what the system player shows.
//
// Bonus: the export bakes in the track's preferred transform, so the output is already
// correctly rotated and carries no display-matrix side data for ffmpeg to misread.
//
// Note: AVMutableVideoComposition and export() emit deprecation warnings on recent macOS
// (the replacements are AVVideoComposition.Configuration and export(to:as:)). This version is
// kept because it is the one actually verified end to end; migrate when you can retest.

import AVFoundation
import Foundation

guard CommandLine.arguments.count == 3 else {
    print("usage: swift tosdr.swift <input> <output.mov>")
    exit(2)
}

let src = URL(fileURLWithPath: CommandLine.arguments[1])
let dst = URL(fileURLWithPath: CommandLine.arguments[2])
try? FileManager.default.removeItem(at: dst)

let asset = AVURLAsset(url: src)
let sem = DispatchSemaphore(value: 0)

Task {
    let vc = try await AVMutableVideoComposition.videoComposition(withPropertiesOf: asset)
    // Forcing a Rec.709 SDR pipeline is what triggers AVFoundation's HDR tone mapping.
    vc.colorPrimaries        = AVVideoColorPrimaries_ITU_R_709_2
    vc.colorTransferFunction = AVVideoTransferFunction_ITU_R_709_2
    vc.colorYCbCrMatrix      = AVVideoYCbCrMatrix_ITU_R_709_2

    guard let ex = AVAssetExportSession(asset: asset,
                                        presetName: AVAssetExportPresetHighestQuality) else {
        print("could not create export session"); exit(1)
    }
    ex.outputURL = dst
    ex.outputFileType = .mov
    ex.videoComposition = vc
    await ex.export()
    if let e = ex.error { print("ERROR: \(e)"); exit(1) }
    print("exported \(dst.path)")
    sem.signal()
}
sem.wait()
