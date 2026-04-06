"""Tests for domain entities: Student and PageInfo."""

import pytest
from school_app.domain.entities import Student, PageInfo


class TestStudent:
    """Tests for the Student dataclass."""

    def test_default_values(self):
        student = Student()
        assert student.school == "________"
        assert student.name == "________"
        assert student.grade == "________"
        assert student.city == "________"

    def test_custom_values(self):
        student = Student(
            school="Школа №1",
            name="Иванов Иван",
            grade="10А",
            city="Москва"
        )
        assert student.school == "Школа №1"
        assert student.name == "Иванов Иван"
        assert student.grade == "10А"
        assert student.city == "Москва"

    def test_partial_custom_values(self):
        student = Student(name="Петров Петр")
        assert student.name == "Петров Петр"
        assert student.school == "________"

    def test_equality(self):
        s1 = Student(name="Иванов Иван")
        s2 = Student(name="Иванов Иван")
        assert s1 == s2

    def test_inequality(self):
        s1 = Student(name="Иванов Иван")
        s2 = Student(name="Петров Петр")
        assert s1 != s2


class TestPageInfo:
    """Tests for the PageInfo dataclass."""

    def test_create_page(self):
        page = PageInfo(title="Главная", content="Добро пожаловать")
        assert page.title == "Главная"
        assert page.content == "Добро пожаловать"

    def test_html_content(self):
        page = PageInfo(
            title="О школе",
            content="<p>Информация о школе</p>"
        )
        assert "<p>" in page.content

    def test_equality(self):
        p1 = PageInfo(title="Тест", content="Контент")
        p2 = PageInfo(title="Тест", content="Контент")
        assert p1 == p2

    def test_inequality(self):
        p1 = PageInfo(title="Тест", content="Контент 1")
        p2 = PageInfo(title="Тест", content="Контент 2")
        assert p1 != p2
