"""Copy the cutest picture entry into the output directory."""

import os
import shutil
from pathlib import Path  # entry.png holds JPEG bytes; format is told apart by magic bytes

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
