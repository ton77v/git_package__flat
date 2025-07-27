import sys
from pathlib import Path

from .src.start_dev import start_dev

sys.path.append((Path(__file__).parent / "src").as_posix())

__all__ = ["start_dev"]