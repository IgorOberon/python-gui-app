"""Main application window that assembles all view components.

This is the composition root of the presentation layer.
It receives domain entities and infrastructure implementations
via dependency injection and wires the views together.
"""

from pathlib import Path
from typing import Optional

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

from school_app.domain.entities import Student, PageInfo
from school_app.domain.repository import ImageRepository
from school_app.presentation.styles import STYLESHEET
from school_app.presentation.views import HeaderView, StudentCardView, InfoPanelView, NavBarView


class MainWindow(QMainWindow):
    """Top-level application window.

    Composes HeaderView, StudentCardView, InfoPanelView, and NavBarView
    into a single layout. Receives all dependencies through the constructor
    to maintain separation from domain and infrastructure layers.
    """

    def __init__(self, student: Student, pages: list[PageInfo],
                 image_repo: ImageRepository, image_path: Optional[Path] = None):
        """Initialize the main window with all dependencies.

        Args:
            student: Student entity for the card view.
            pages: List of PageInfo objects for the info panel.
            image_repo: Repository implementation for loading photos.
            image_path: Optional path to the student photo file.
        """
        super().__init__()

        self.setWindowTitle("Моя школа и наш класс")
        self.resize(1100, 750)
        self.setMinimumSize(1100, 750)
        self.setStyleSheet(STYLESHEET)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)

        header = HeaderView()
        main_layout.addWidget(header)

        middle_layout = QHBoxLayout()
        middle_layout.setSpacing(20)

        student_card = StudentCardView(student, image_repo, image_path)
        info_panel = InfoPanelView(pages)

        middle_layout.addWidget(student_card)
        middle_layout.addWidget(info_panel, stretch=1)

        main_layout.addLayout(middle_layout)

        button_names = ["Главная", "О школе", "О классе", "Обо мне", "Увлечения", "Мечта"]
        nav_bar = NavBarView(button_names, info_panel.stacked)
        main_layout.addWidget(nav_bar)

        central.setLayout(main_layout)
