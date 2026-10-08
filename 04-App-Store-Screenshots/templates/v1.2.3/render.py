#!/usr/bin/env python3
"""Compose v1.2.3 native captures using TubeBoard's existing licensed treatment.

No generated or repainted product UI. Full native captures retain their aspect
ratio. Header/search artwork uses the same source images on exact Apple canvases.
"""
from pathlib import Path
import argparse, importlib.util, subprocess, tempfile

STORIES = {
    "01-live-board.png": ("Your next train", "Live London departures at a glance"),
    "02-follow-train.png": ("Follow your train", "Premium: route and live progress where available"),
    "03-next-departures.png": ("Every platform", "Premium: compare next departures within each direction"),
    "04-overground.png": ("London Overground", "All six named lines join the free live board"),
    "05-by-destination.png": ("Heading your way", "Premium: group your station's trains by destination"),
    "06-home-status.png": ("Every journey", "Recent stations and line status together"),
}
def call(args):
    subprocess.run(args, check=True, capture_output=True)

def creative(raw, output, font, size, placement, work):
    width, height = size
    phone, duo = work / "creative-phone.png", work / "creative-duo.png"
    if placement == "header":
        phone_height, duo_width = 1250, 1570
        phone_xy, duo_xy = (1390, 205), (2045, 435)
        title, title_width, title_points, title_xy = "Your next\ntrain.", 1140, 185, (190, 450)
        sub, sub_xy = "Live London departures.\nDesigned for iPhone Duo.", (195, 1070)
    else:
        phone_height, duo_width = 1900, 1450
        phone_xy, duo_xy = (1220, 390), (2160, 925)
        title, title_width, title_points, title_xy = "Your next\ntrain.", 1030, 195, (175, 490)
        sub, sub_xy = "Live London departures.\nAn adaptable Duo workspace.", (180, 1420)
    call(["magick", str(raw / "iphone-medium/01-live-board.png"), "-resize", f"x{phone_height}", str(phone)])
    call(["magick", str(raw / "duo/02-inner-workspace-landscape.png"), "-resize", f"{duo_width}x", str(duo)])
    headline, subtitle = work / "creative-head.png", work / "creative-sub.png"
    call(["magick", "-background", "none", "-fill", "#FF9729", "-font", str(font),
          "-pointsize", str(title_points), "-size", f"{title_width}x", f"caption:{title}", str(headline)])
    call(["magick", "-background", "none", "-fill", "#A9A9B2", "-font", "/System/Library/Fonts/HelveticaNeue.ttc",
          "-pointsize", "61", "-size", "1030x", f"caption:{sub}", str(subtitle)])
    args=["magick", "-size", f"{width}x{height}", "gradient:#17130F-#050507", "-gravity", "northwest"]
    for path, (x,y) in [(headline,title_xy),(subtitle,sub_xy),(phone,phone_xy),(duo,duo_xy)]:
        args += [str(path),"-geometry",f"+{x}+{y}","-compose","over","-composite"]
    args += ["-alpha","remove","-alpha","off","-depth","8",f"PNG24:{output}"]
    call(args)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--app-root",type=Path,required=True)
    parser.add_argument("--raw",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise SystemExit("Output exists; preserve prior rendered assets and choose a fresh directory.")
    source=args.app_root/"scripts/compose_app_store_screenshots.py"
    spec=importlib.util.spec_from_file_location("tubeboard_canonical_screenshot_composer",source)
    composer=importlib.util.module_from_spec(spec);spec.loader.exec_module(composer)
    args.output.mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix="tubeboard-v123-art-") as tmp:
        work=Path(tmp)
        for device,size in [("iphone-medium",(1206,2622)),("ipad-13",(2064,2752))]:
            folder=args.output/device;folder.mkdir()
            for name,(headline,subline) in STORIES.items():
                src=args.raw/device/name
                if not src.is_file():raise SystemExit(f"Missing native source: {src}")
                composer.compose_v12_frame(src,folder/name,headline,subline,size,work)
        duo=args.output/"duo";duo.mkdir()
        for name,headline,subline,size in [
            ("01-outer-board.png","Made for iPhone Duo","Station controls, right where you need them",(1398,2034)),
            ("02-inner-workspace-landscape.png","Room for your journey","Stations and your board stay clear of the fold",(2853,2007))]:
            composer.compose_v12_frame(args.raw/"duo"/name,duo/name,headline,subline,size,work)
        extras=args.output/"creative-assets";extras.mkdir()
        creative(args.raw,extras/"01-product-page-header.png",composer.FONT_HEAD,(3840,1646),"header",work)
        creative(args.raw,extras/"02-search-results.png",composer.FONT_HEAD,(3840,2560),"search",work)
        watch=args.output/"watch-46";watch.mkdir()
        for name in ["01-nearby-stations.png","02-live-board.png"]:
            source=args.raw/"watch-46"/name
            dimensions=subprocess.check_output(["magick","identify","-format","%wx%h",str(source)],text=True)
            if dimensions!="416x496":raise SystemExit(f"Unsupported Watch source geometry: {dimensions}")
            call(["magick",str(source),"-alpha","remove","-alpha","off","-depth","8",f"PNG24:{watch/name}"])
    print("Rendered eighteen exact-size screenshot and creative images; visual review and source provenance remain required.")

if __name__=="__main__":main()
