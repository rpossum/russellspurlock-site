#!/usr/bin/env python3
"""
Generate a printable QR PNG for https://russellspurlock.com/card.

One-off utility — run when the card URL changes or you need a new print asset.

Install deps (one time):
    pip install "qrcode[pil]"

Run:
    python scripts/generate-qr.py

Output: card-qr.png in the current directory (1200x1200, site-blue on white,
high error correction so it tolerates a logo overlay or print smudging).
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://russellspurlock.com/card"
OUTFILE = "card-qr.png"
FG = "#004080"
BG = "white"

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_H,
    box_size=40,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color=FG, back_color=BG)
img.save(OUTFILE)

print(f"Wrote {OUTFILE} -> {URL}")
