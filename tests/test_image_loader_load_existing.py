"""Tests for loading an actual image file via QtImageLoader."""

import base64
from pathlib import Path
import tempfile

import pytest

from school_app.infrastructure.image_loader import QtImageLoader
from PyQt6.QtGui import QPixmap


def _write_minimal_png(path: Path) -> None:
    # Minimal 1x1 PNG base64 data
    data = base64.b64decode(
        'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGMAAQAABQABDQottQAAAABJRU5ErkJggg=='
    )
    path.write_bytes(data)


def test_load_existing_image(tmp_path: Path):
    loader = QtImageLoader()
    img_path = tmp_path / "tiny.png"
    _write_minimal_png(img_path)
    pix = loader.load_photo(img_path)
    assert isinstance(pix, QPixmap)
    assert not pix.isNull()
