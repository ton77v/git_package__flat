import sys
from pathlib import Path

sys.path.append((Path(__file__).parent / "src").as_posix())

from .src.start_dev import start_dev  # should be after the path extension

__all__ = ["start_dev"]