"""Header view displaying the application title and subtitle."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class HeaderView(QFrame):
    """Top header section with app title and subtitle.

    Renders a centered title "Моя школа и наш класс" and a subtitle
    "Сделано на Python и PyQt6" inside a styled QFrame.
    """

    def __init__(self, parent=None):
        """Initialize the header view.

        Args:
            parent: Optional parent widget.
        """
        super().__init__(parent)
        self.setObjectName("header")
        self.setFixedHeight(110)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(4)

        title = QLabel("Моя школа и наш класс")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Сделано на Python и PyQt6")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        self.setLayout(layout)
