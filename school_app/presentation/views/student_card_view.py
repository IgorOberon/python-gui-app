"""Student card view displaying personal info and photo."""

from pathlib import Path
from typing import Optional

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QCursor

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

        # Make photo area clickable to load a new image
        self.image_repo = image_repo
        self._student = student
        self._photo_path = image_path if image_path else None
        self.photo_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.photo_label.installEventFilter(self)

        # Prepare container for editable fields to allow updates from persisted data
        self._editable_fields = {}
        # Load persisted data on startup (if any)
        persisted = None
        try:
            from school_app.persistence.json_store import load_student
            persisted = load_student()
        except Exception:
            persisted = None
        # Editable fields for inline editing + persistence
        def _on_update(field_name, new_value):
            setattr(student, field_name, new_value)
            # Preserve any existing photo_path from last persisted state or UI
            try:
                from school_app.persistence.json_store import load_student as _load
            except Exception:
                _load = None
            photo_path = getattr(self, "_photo_path", None)
            if _load:
                last = _load()
                if last and getattr(last, "photo_path", None):
                    photo_path = last.photo_path
            persisted = PersistedStudent(
                school=student.school,
                name=student.name,
                grade=student.grade,
                city=student.city,
                photo_path=photo_path,
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
        for label_text, value, field_key in fields:
            ef = EditableField(label_text, value, _on_update, field_key=field_key)
            ef.edited.connect(_on_update)
            self._editable_fields[field_key] = ef
            layout.addWidget(ef)

        # Apply persisted values to UI fields if available
        if persisted:
            try:
                if 'school' in self._editable_fields:
                    self._editable_fields['school'].set_value(persisted.school)
                if 'name' in self._editable_fields:
                    self._editable_fields['name'].set_value(persisted.name)
                if 'grade' in self._editable_fields:
                    self._editable_fields['grade'].set_value(persisted.grade)
                if 'city' in self._editable_fields:
                    self._editable_fields['city'].set_value(persisted.city)
                if getattr(persisted, 'photo_path', None):
                    pp = Path(str(persisted.photo_path))
                    if pp.exists():
                        pix = self.image_repo.load_photo(pp)
                        if pix:
                            scaled = pix.scaled(
                                120, 120,
                                Qt.AspectRatioMode.KeepAspectRatio,
                                Qt.TransformationMode.SmoothTransformation
                            )
                            self.photo_label.setPixmap(scaled)
            except Exception:
                pass

        layout.addStretch()
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj is self.photo_label and event.type() == QEvent.Type.MouseButtonPress:
            self._open_photo_dialog()
            return True
        return super().eventFilter(obj, event)

    def _open_photo_dialog(self, event=None):
        # Lazy import to avoid hard GUI dependency when testing non-GUI paths
        try:
            from PyQt6.QtWidgets import QFileDialog
        except Exception:
            return
        from pathlib import Path
        path, _ = QFileDialog.getOpenFileName(self, "Выбрать фото ученика", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if not path:
            return
        p = Path(path)
        self._photo_path = p
        pix = self.image_repo.load_photo(p)
        if pix:
            scaled = pix.scaled(
                120, 120,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.photo_label.setPixmap(scaled)
        # Persist path
        try:
            persisted = PersistedStudent(
                school=self._student.school,
                name=self._student.name,
                grade=self._student.grade,
                city=self._student.city,
                photo_path=str(p),
            )
            save_student(persisted)
        except Exception:
            pass
