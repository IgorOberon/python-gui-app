import sys
import os
from functools import partial
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QPushButton, QTextBrowser, QStackedWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Моя школа и наш класс")
        self.resize(1100, 750)
        self.setMinimumSize(1100, 750)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0f172a;
            }
            QFrame#header, QFrame#card, QFrame#buttons {
                background-color: #1e293b;
                border-radius: 16px;
            }
            QLabel#title {
                color: #f1f5f9;
                font-size: 26px;
                font-weight: bold;
            }
            QLabel#subtitle {
                color: #64748b;
                font-size: 14px;
            }
            QLabel#card-title {
                color: #3b82f6;
                font-size: 18px;
                font-weight: bold;
            }
            QLabel#field-label {
                color: #f1f5f9;
                font-size: 14px;
                font-weight: bold;
            }
            QLabel#field-value {
                color: #94a3b8;
                font-size: 14px;
            }
            QFrame#divider {
                background-color: #334155;
                max-height: 1px;
            }
            QLabel#photo-placeholder {
                background-color: #334155;
                color: #94a3b8;
                border: 2px dashed #475569;
                border-radius: 12px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3b82f6;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
            }
            QTextBrowser {
                background-color: #1e293b;
                color: #f1f5f9;
                border: none;
                border-radius: 16px;
                padding: 24px;
                font-size: 16px;
            }
        """)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)

        # --- TOP: Header ---
        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(110)

        header_layout = QVBoxLayout()
        header_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.setSpacing(4)

        title = QLabel("Моя школа и наш класс")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title)

        subtitle = QLabel("Сделано на Python и PyQt6")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(subtitle)

        header.setLayout(header_layout)
        main_layout.addWidget(header)

        # --- MIDDLE: Left card + Right info panel ---
        middle_layout = QHBoxLayout()
        middle_layout.setSpacing(20)

        # Left: Student card
        student_card = QFrame()
        student_card.setObjectName("card")
        student_card.setFixedWidth(300)

        student_layout = QVBoxLayout()
        student_layout.setContentsMargins(24, 24, 24, 24)
        student_layout.setSpacing(20)

        card_title = QLabel("Карточка ученика")
        card_title.setObjectName("card-title")
        card_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        student_layout.addWidget(card_title)

        # Photo area
        self.photo_label = QLabel()
        self.photo_label.setObjectName("photo-placeholder")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setFixedSize(120, 120)
        self.photo_label.setText("Фото\nученика")
        student_layout.addWidget(self.photo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Load image if it exists
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "student.jpg")
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path).scaled(
                120, 120,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.photo_label.setPixmap(pixmap)
            self.photo_label.setStyleSheet("background: transparent; border: none;")

        divider = QFrame()
        divider.setObjectName("divider")
        student_layout.addWidget(divider)

        for label_text, value in [
            ("Школа:", "________"),
            ("Ученик:", "________"),
            ("Класс:", "________"),
            ("Город:", "________"),
        ]:
            row = QHBoxLayout()

            lbl = QLabel(label_text)
            lbl.setObjectName("field-label")
            row.addWidget(lbl)

            val = QLabel(value)
            val.setObjectName("field-value")
            row.addWidget(val, stretch=1)

            student_layout.addLayout(row)

        student_layout.addStretch()
        student_card.setLayout(student_layout)

        # Right: Stacked widget
        self.stacked = QStackedWidget()

        pages = [
            ("Приветствуем!", "Это приложение поможет вам следить за школьными событиями, узнавать новости класса и быть в курсе всех изменений.<br><br>Заполните карточку ученика слева, чтобы начать работу."),
            ("О школе", "Здесь будет информация о нашей школе, учителях и расписании уроков."),
            ("О классе", "Здесь будет информация о нашем классе, одноклассниках и классном руководителе."),
            ("Обо мне", "Здесь будет личная информация: любимые предметы, оценки и достижения."),
            ("Увлечения", "Здесь будут мои хобби, кружки и секции."),
            ("Мечта", "Здесь будет моя мечта и цели на будущее."),
        ]

        for heading, text in pages:
            browser = QTextBrowser()
            browser.setHtml(
                f"<h2 style='color: #3b82f6; font-size: 24px;'>{heading}</h2>"
                f"<hr style='border: 1px solid #334155; margin: 16px 0;'>"
                f"<p style='color: #cbd5e1; font-size: 16px; line-height: 1.6;'>{text}</p>"
            )
            self.stacked.addWidget(browser)

        info_panel = QFrame()
        info_panel.setObjectName("card")
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.addWidget(self.stacked)
        info_panel.setLayout(info_layout)

        middle_layout.addWidget(student_card)
        middle_layout.addWidget(info_panel, stretch=1)

        main_layout.addLayout(middle_layout)

        # --- BOTTOM: Buttons ---
        buttons_frame = QFrame()
        buttons_frame.setObjectName("buttons")
        buttons_frame.setFixedHeight(70)

        buttons_layout = QHBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttons_layout.setSpacing(12)
        buttons_layout.setContentsMargins(20, 12, 20, 12)

        button_names = ["Главная", "О школе", "О классе", "Обо мне", "Увлечения", "Мечта"]

        for i, name in enumerate(button_names):
            btn = QPushButton(name)
            btn.clicked.connect(partial(self.stacked.setCurrentIndex, i))
            buttons_layout.addWidget(btn)

        buttons_frame.setLayout(buttons_layout)
        main_layout.addWidget(buttons_frame)

        central.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
