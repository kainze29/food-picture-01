"""food-picture-01 entry: copy the bundled ramen photograph to /output/entry.png.

The image is a JPEG (1024x1024, under 1 MiB). The rules allow a JPEG whose
bytes are written to entry.png, and the copy is byte-for-byte deterministic,
so two runs produce identical output. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "food.jpg"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
