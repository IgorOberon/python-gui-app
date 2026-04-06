"""Student card view displaying personal info and photo."""

from pathlib import Path
from typing import Optional

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from school_app.domain.entities import Student
from school_app.domain.repository import ImageRepository
from school_app.presentation.views.editable_field import EditableField
from school_app.persistence.json_store import PersistedStudent, save_student


class StudentCardView(QFrame):
    """Left-side card showing student photo, name, school, grade, and city.

    Displays a photo placeholder (or loaded image) followed by
    labeled student fields. Photo loading is delegated to an
    ImageRepository to keep the view decoupled from image libraries.
    """

    def __init__(self, student: Student, image_repo: ImageRepository, image_path: Optional[Path] = None, parent=None):
        """Initialize the student card view.

        Args:
            student: Student entity with school, name, grade, city.
            image_repo: Repository for loading the student photo.
            image_path: Optional path to the student photo file.
            parent: Optional parent widget.
        """
        super().__init__(parent)
        self.setObjectName("card")
        self.setFixedWidth(300)

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        card_title = QLabel("Карточка ученика")
        card_title.setObjectName("card-title")
        card_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(card_title)

        self.photo_label = QLabel()
        self.photo_label.setObjectName("photo-placeholder")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setFixedSize(120, 120)
        self.photo_label.setText("Фото\nученика")
        layout.addWidget(self.photo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        if image_path:
            pixmap = image_repo.load_photo(image_path)
            if pixmap:
                scaled = pixmap.scaled(
                    120, 120,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.photo_label.setPixmap(scaled)
                self.photo_label.setStyleSheet("background: transparent; border: none;")

        divider = QFrame()
        divider.setObjectName("divider")
        layout.addWidget(divider)

        # Editable fields for inline editing + persistence
        def _on_update(field_name, new_value):
            setattr(student, field_name, new_value)
            persisted = PersistedStudent(
                school=student.school,
                name=student.name,
                grade=student.grade,
                city=student.city,
            )
            try:
                save_student(persisted)
            except Exception:
                pass

        fields = [
            ("Школа", student.school, 'school'),
            ("Ученик", student.name, 'name'),
            ("Класс", student.grade, 'grade'),
            ("Город", student.city, 'city'),
        ]
        for label_text, value, field in fields:
            ef = EditableField(label_text, value, _on_update)
            layout.addWidget(ef)

        layout.addStretch()
        self.setLayout(layout)
