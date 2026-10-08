#!/usr/bin/env python3
"""Export actual Duo footage; omit launch, preserve full UI and source clock."""
import argparse, subprocess
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--native',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
if a.output.exists():raise SystemExit('Preserve previous exports; choose a fresh output.')
a.output.parent.mkdir(parents=True,exist_ok=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss','4','-i',str(a.native),
 '-t','15.9','-vf','scale=886:-2:flags=lanczos,pad=886:1920:(ow-iw)/2:(oh-ih)/2:color=0x050507,fps=30',
 '-an','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','18',
 '-movflags','+faststart',str(a.output)],check=True)
