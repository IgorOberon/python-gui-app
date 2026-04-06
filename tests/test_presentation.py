"""Tests for the presentation layer: styles and page creation."""

import pytest
from school_app.presentation.styles import STYLESHEET
from school_app.main import create_student, create_pages
from school_app.domain.entities import Student, PageInfo


class TestStylesheet:
    """Tests for the QSS stylesheet."""

    def test_stylesheet_is_string(self):
        assert isinstance(STYLESHEET, str)

    def test_stylesheet_not_empty(self):
        assert len(STYLESHEET.strip()) > 0

    def test_contains_main_window_style(self):
        assert "QMainWindow" in STYLESHEET

    def test_contains_button_style(self):
        assert "QPushButton" in STYLESHEET

    def test_contains_label_style(self):
        assert "QLabel" in STYLESHEET

    def test_contains_frame_style(self):
        assert "QFrame" in STYLESHEET

    def test_contains_dark_theme_colors(self):
        assert "#0f172a" in STYLESHEET
        assert "#1e293b" in STYLESHEET


class TestCreateStudent:
    """Tests for the create_student factory function."""

    def test_returns_student_instance(self):
        student = create_student()
        assert isinstance(student, Student)

    def test_returns_default_values(self):
        student = create_student()
        assert student.school == "________"
        assert student.name == "________"

    def test_returns_new_instance_each_time(self):
        s1 = create_student()
        s2 = create_student()
        assert s1 is not s2


class TestCreatePages:
    """Tests for the create_pages factory function."""

    def test_returns_list(self):
        pages = create_pages()
        assert isinstance(pages, list)

    def test_returns_six_pages(self):
        pages = create_pages()
        assert len(pages) == 6

    def test_all_pages_are_page_info(self):
        pages = create_pages()
        assert all(isinstance(p, PageInfo) for p in pages)

    def test_first_page_is_welcome(self):
        pages = create_pages()
        assert pages[0].title == "Приветствуем!"

    def test_page_titles(self):
        pages = create_pages()
        expected_titles = [
            "Приветствуем!",
            "О школе",
            "О классе",
            "Обо мне",
            "Увлечения",
            "Мечта"
        ]
        actual_titles = [p.title for p in pages]
        assert actual_titles == expected_titles

    def test_pages_have_content(self):
        pages = create_pages()
        assert all(len(p.content) > 0 for p in pages)

    def test_pages_are_new_instances(self):
        pages1 = create_pages()
        pages2 = create_pages()
        assert pages1 is not pages2
        assert pages1[0] is not pages2[0]
