"""Application entry point.

Creates domain entities, infrastructure implementations,
and bootstraps the PyQt6 application.
"""

import sys
import os
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from school_app.domain.entities import Student, PageInfo
from school_app.infrastructure.image_loader import QtImageLoader
from school_app.presentation.main_window import MainWindow


def create_student() -> Student:
    """Create a default Student entity with placeholder values.

    Returns:
        Student instance with all fields set to placeholder strings.
    """
    return Student()


def create_pages() -> list[PageInfo]:
    """Create the list of info panel pages.

    Returns:
        List of six PageInfo objects: welcome, school, class, about me,
        hobbies, and dream.
    """
    return [
        PageInfo(
            title="Приветствуем!",
            content="Это приложение поможет вам следить за школьными событиями, узнавать новости класса и быть в курсе всех изменений.<br><br>Заполните карточку ученика слева, чтобы начать работу.",
        ),
        PageInfo(
            title="О школе",
            content="Здесь будет информация о нашей школе, учителях и расписании уроков.",
        ),
        PageInfo(
            title="О классе",
            content="Здесь будет информация о нашем классе, одноклассниках и классном руководителе.",
        ),
        PageInfo(
            title="Обо мне",
            content="Здесь будет личная информация: любимые предметы, оценки и достижения.",
        ),
        PageInfo(
            title="Увлечения",
            content="Здесь будут мои хобби, кружки и секции.",
        ),
        PageInfo(
            title="Мечта",
            content="Здесь будет моя мечта и цели на будущее.",
        ),
    ]


def main():
    """Create and run the PyQt6 application.

    Initializes QApplication, creates all dependencies,
    assembles the MainWindow, and starts the event loop.
    """
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    student = create_student()
    pages = create_pages()
    image_repo = QtImageLoader()

    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    image_path = script_dir / "student.jpg"

    window = MainWindow(
        student=student,
        pages=pages,
        image_repo=image_repo,
        image_path=image_path if image_path.exists() else None,
    )
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
