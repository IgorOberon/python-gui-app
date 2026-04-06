"""Navigation bar with buttons for switching info panel pages."""

from functools import partial

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class NavBarView(QFrame):
    """Bottom navigation bar with buttons that switch the stacked widget index.

    Each button corresponds to a page in the info panel. Clicking a button
    calls ``setCurrentIndex`` on the provided QStackedWidget.
    """

    def __init__(self, button_names: list[str], target_stacked, parent=None):
        """Initialize the navigation bar.

        Args:
            button_names: Labels for each navigation button.
            target_stacked: QStackedWidget whose index changes on button click.
            parent: Optional parent widget.
        """
        super().__init__(parent)
        self.setObjectName("buttons")
        self.setFixedHeight(70)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 12, 20, 12)

        for i, name in enumerate(button_names):
            btn = QPushButton(name)
            btn.clicked.connect(partial(target_stacked.setCurrentIndex, i))
            layout.addWidget(btn)

        self.setLayout(layout)
