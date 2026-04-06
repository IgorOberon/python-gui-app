"""Qt stylesheet for the school application.

Contains the complete QSS stylesheet applied to the main window,
defining the dark theme appearance for all widgets.
"""

STYLESHEET = """
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
"""
