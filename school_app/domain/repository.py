"""Abstract repository interfaces for infrastructure dependencies.

Defines contracts that infrastructure implementations must fulfill,
ensuring the domain layer remains independent of external frameworks.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class ImageRepository(ABC):
    """Abstract interface for loading image files from the filesystem.

    Implementations should handle the actual image loading logic
    using a specific library (e.g., PyQt6 QPixmap, PIL).
    """

    @abstractmethod
    def load_photo(self, path: Path) -> Optional[object]:
        """Load an image from the given file path.

        Args:
            path: Path to the image file.

        Returns:
            Loaded image object, or None if the file does not exist.
        """
        pass
