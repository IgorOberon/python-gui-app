"""Simple JSON-based persistence for the student data."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional


DATA_PATH = Path(__file__).resolve().parents[2] / "student_data.json"


@dataclass
class PersistedStudent:
    school: str
    name: str
    grade: str
    city: str
    photo_path: Optional[str] = None


def load_student() -> Optional[PersistedStudent]:
    if not DATA_PATH.exists():
        return None
    with DATA_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return PersistedStudent(**data)


def save_student(student: PersistedStudent) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(asdict(student), f, ensure_ascii=False, indent=2)
