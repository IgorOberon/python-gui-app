"""PyQt6-based implementation of the image loading repository."""

from pathlib import Path
from typing import Optional

from PyQt6.QtGui import QPixmap

from school_app.domain.repository import ImageRepository


class QtImageLoader(ImageRepository):
    """Loads images using PyQt6 QPixmap.

    Implements ImageRepository by delegating to QPixmap for
    image file reading. Returns None if the file doesn't exist.
    """

    def load_photo(self, path: Path) -> Optional[QPixmap]:
        """Load an image file as a QPixmap.

        Args:
            path: Path to the image file.

        Returns:
            QPixmap of the loaded image, or None if file not found.
        """
        if not path.exists():
            return None
        return QPixmap(str(path))
