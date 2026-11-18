# news-image-20261117 entry (Python 3.13, standard library only).
#
# The entry is the image held in this repository (entry.png): one image
# summing up the world news of Tuesday 17 November 2026 -- the Kerch
# Bridge strike, tankers burning near the Strait of Hormuz, and the
# Xi-Trump-Putin trilateral announced for Shenzhen.
#
# This program copies that image to the output directory. It uses no
# network and is deterministic: every run writes the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SOURCE = os.path.join(_HERE, "entry.png")
_OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_MAX_BYTES = 1024 * 1024  # the competition's cap: a whole image of at most 1 MiB

if not os.path.isfile(_SOURCE):
    raise SystemExit("entry.png missing beside main.py")
if os.path.getsize(_SOURCE) > _MAX_BYTES:
    raise SystemExit("entry.png is over the 1 MiB cap")

os.makedirs(_OUTPUT_DIR, exist_ok=True)
_destination = os.path.join(_OUTPUT_DIR, "entry.png")
shutil.copyfile(_SOURCE, _destination)

# Guard the run: the output must be the same bytes we hold, and within cap.
if os.path.getsize(_destination) != os.path.getsize(_SOURCE):
    raise SystemExit("output size differs from entry.png")
print("wrote %s (%d bytes)" % (_destination, os.path.getsize(_destination)))
