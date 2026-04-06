"""Inline editable field component used in StudentCardView."""
from __future__ import annotations

from typing import Callable

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt


class EditableField(QFrame):
    def __init__(self, label_text: str, value: str, on_update: Callable[[str, str], None], parent=None):
        super().__init__(parent)
        self.label_text = label_text
        self.on_update = on_update
        self.setFrameShape(QFrame.NoFrame)
        self._init_ui(value)

    def _init_ui(self, value: str):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.lbl = QLabel(f"{self.label_text}:")
        self.lbl.setObjectName("field-label")
        self.layout.addWidget(self.lbl)

        self.value_label = QLabel(value)
        self.value_label.setObjectName("field-value")
        self.value_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.layout.addWidget(self.value_label, stretch=1)

        self.editor = QLineEdit(value)
        self.editor.hide()
        self.layout.addWidget(self.editor, stretch=1)

        # Double-click to edit
        self.value_label.mouseDoubleClickEvent = self._start_edit  # type: ignore
        self.editor.editingFinished.connect(self._finish_edit)

    def _start_edit(self, event):
        self.value_label.hide()
        self.editor.setText(self.value_label.text())
        self.editor.show()
        self.editor.setFocus()

    def _finish_edit(self):
        new_text = self.editor.text()
        self.value_label.setText(new_text)
        self.editor.hide()
        self.value_label.show()
        # Notify container about update: field name without the trailing colon
        self.on_update(self.label_text, new_text)

    def set_value(self, value: str):
        self.value_label.setText(value)
        self.editor.setText(value)
