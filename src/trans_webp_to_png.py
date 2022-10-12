#!/usr/bin/env python3
"""
https://developers.google.com/speed/webp/docs/cwebp
https://developers.google.com/speed/webp/docs/dwebp
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html
"""

import os
import subprocess
from glob import glob

LIBWEBP = 'D:/libwebp-1.2.4-windows-x64/bin'

for _ in glob('*.webp'):
    filename = os.path.splitext(os.path.basename(_))[0]
    subprocess.run(
        f'{LIBWEBP}/cwebp.exe {_} -o {filename}.webp',
        shell=True,
        check=True
    )
    subprocess.run(
        f'{LIBWEBP}/dwebp.exe {filename}.webp -o {filename}.png',
        shell=True,
        check=True
    )
