#!/usr/bin/env python3
"""Actual native Duo footage, with Apple's specified enabled stereo AAC track."""
from pathlib import Path
import argparse,subprocess
p=argparse.ArgumentParser();p.add_argument('--native',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
if a.output.exists():raise SystemExit('Preserve prior exports; choose a fresh output.')
a.output.parent.mkdir(parents=True,exist_ok=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss','4','-i',str(a.native),
 '-f','lavfi','-i','anullsrc=channel_layout=stereo:sample_rate=48000','-t','15.9',
 '-map','0:v:0','-map','1:a:0','-vf','scale=886:-2:flags=lanczos,pad=886:1920:(ow-iw)/2:(oh-ih)/2:color=0x050507,fps=30',
 '-c:v','libx264','-profile:v','high','-level:v','4.0','-pix_fmt','yuv420p',
 '-b:v','10M','-minrate','10M','-maxrate','10M','-bufsize','20M','-x264-params','nal-hrd=cbr:force-cfr=1',
 '-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709',
 '-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-disposition:a:0','default',
 '-movflags','+faststart',str(a.output)],check=True)
