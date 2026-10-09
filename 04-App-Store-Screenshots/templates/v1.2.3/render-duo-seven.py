#!/usr/bin/env python3
"""Seven complete native Duo frames, matching the existing six-device story."""
from pathlib import Path
import argparse,importlib.util,tempfile
from render import STORIES
p=argparse.ArgumentParser();p.add_argument('--app-root',type=Path,required=True);p.add_argument('--raw',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
if a.output.exists():raise SystemExit('Preserve previous exports; choose a fresh directory.')
spec=importlib.util.spec_from_file_location('canonical',a.app_root/'scripts/compose_app_store_screenshots.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);a.output.mkdir(parents=True)
with tempfile.TemporaryDirectory(prefix='tubeboard-duo-seven-') as td:
 w=Path(td)
 c.compose_v12_frame(a.raw/'00-made-for-duo.png',a.output/'00-made-for-duo.png','Made for iPhone Duo','Stations, your live board and Premium Follow a Train together',(2853,2007),w)
 for name,(head,sub) in STORIES.items():c.compose_v12_frame(a.raw/name,a.output/name,head,sub,(1398,2034),w)
print('Seven Duo images rendered; full UI preserved, exact standard captions reused.')
