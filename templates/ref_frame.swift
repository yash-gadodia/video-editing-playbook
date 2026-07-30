// Extract system-tone-mapped reference stills from a video, i.e. exactly what the OS
// video player and photo viewer show. Use these as ground truth before judging any grade.
//
//   swift ref_frame.swift input.MOV 5 12 30      -> ref_5.png ref_12.png ref_30.png
//
// The trap this defends against: a hand-rolled colour transform that looks "richer" than a
// naive decode feels correct and is not. Put your render beside the system reference and look.
// If you are fitting a transform numerically, score against these frames; a best fit that sits
// at the edge of your parameter grid means the approach is wrong, not the parameters.

import AVFoundation
import AppKit

guard CommandLine.arguments.count >= 3 else {
    print("usage: swift ref_frame.swift <input> <seconds...>")
    exit(2)
}

let url = URL(fileURLWithPath: CommandLine.arguments[1])
let times = CommandLine.arguments.dropFirst(2).compactMap(Double.init)

let gen = AVAssetImageGenerator(asset: AVURLAsset(url: url))
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero          // exact frame, not the nearest keyframe
gen.requestedTimeToleranceAfter = .zero

for sec in times {
    let cg = try! gen.copyCGImage(at: CMTime(seconds: sec, preferredTimescale: 600),
                                  actualTime: nil)
    let data = NSBitmapImageRep(cgImage: cg).representation(using: .png, properties: [:])!
    let out = "ref_\(Int(sec)).png"
    try! data.write(to: URL(fileURLWithPath: out))
    print("\(out)  \(cg.width)x\(cg.height)")
}
