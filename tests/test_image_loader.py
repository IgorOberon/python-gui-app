"""Tests for the image loading infrastructure."""

import pytest
from pathlib import Path
from school_app.infrastructure.image_loader import QtImageLoader


class TestQtImageLoader:
    """Tests for the QtImageLoader implementation."""

    def setup_method(self):
        self.loader = QtImageLoader()

    def test_load_nonexistent_file(self):
        result = self.loader.load_photo(Path("nonexistent.jpg"))
        assert result is None

    def test_load_invalid_path(self):
        result = self.loader.load_photo(Path("/invalid/path/photo.jpg"))
        assert result is None

    def test_load_empty_path_returns_pixmap(self):
        result = self.loader.load_photo(Path(""))
        assert result is not None
