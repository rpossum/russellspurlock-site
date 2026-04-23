#!/usr/bin/env python3
"""
Generate a printable QR PNG for https://russellspurlock.com/card with the
site's plane logo overlaid in the middle.

One-off utility — run when the card URL changes or you need a new print asset.

Install deps (one time):
    pip install "qrcode[pil]"

Run:
    python scripts/generate-qr.py

Output: card-qr.png in the current directory (1640x1640, site-blue on white,
high error correction so the logo overlay in the center is recoverable).
"""

import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

URL = "https://russellspurlock.com/card"
OUTFILE = "card-qr.png"
FG = "#004080"
BG = "white"

# Logo overlay — path is relative to the repo root so the script is
# expected to run from there.
LOGO_PATH = "images-new/plane_blue.png"
LOGO_WIDTH_RATIO = 0.28   # logo spans 28% of QR width
LOGO_PAD = 24             # px of white padding around the logo

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_H,
    box_size=40,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

qr_img = qr.make_image(fill_color=FG, back_color=BG).convert("RGBA")
qw, qh = qr_img.size

if os.path.exists(LOGO_PATH):
    logo = Image.open(LOGO_PATH).convert("RGBA")
    target_w = int(qw * LOGO_WIDTH_RATIO)
    scale = target_w / logo.width
    logo = logo.resize((target_w, int(logo.height * scale)), Image.LANCZOS)

    # White plaque sized to the logo bounding box + padding, so the QR
    # modules under the logo read as solid white (within H error-correction
    # tolerance).
    plaque_w = logo.width + LOGO_PAD * 2
    plaque_h = logo.height + LOGO_PAD * 2
    plaque = Image.new("RGBA", (plaque_w, plaque_h), (255, 255, 255, 255))
    plaque.paste(logo, (LOGO_PAD, LOGO_PAD), logo)

    offset = ((qw - plaque_w) // 2, (qh - plaque_h) // 2)
    qr_img.alpha_composite(plaque, dest=offset)
else:
    print(f"warning: {LOGO_PATH} not found, writing QR without logo overlay")

qr_img.convert("RGB").save(OUTFILE)
print(f"Wrote {OUTFILE} -> {URL}")
