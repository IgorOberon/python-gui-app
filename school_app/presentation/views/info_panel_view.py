"""Info panel view with a stacked widget showing page content."""

from PyQt6.QtWidgets import QFrame, QVBoxLayout
from PyQt6.QtWidgets import QTextBrowser, QStackedWidget

from school_app.domain.entities import PageInfo


class InfoPanelView(QFrame):
    """Right-side panel displaying navigable pages with HTML content.

    Contains a QStackedWidget where each page is a QTextBrowser
    rendered from a PageInfo entity. The stacked widget is exposed
    via the ``stacked`` attribute for external navigation.
    """

    def __init__(self, pages: list[PageInfo], parent=None):
        """Initialize the info panel with a list of pages.

        Args:
            pages: List of PageInfo objects to display as stacked pages.
            parent: Optional parent widget.
        """
        super().__init__(parent)
        self.setObjectName("card")

        self.stacked = QStackedWidget()

        for page in pages:
            browser = QTextBrowser()
            browser.setHtml(
                f"<h2 style='color: #3b82f6; font-size: 24px;'>{page.title}</h2>"
                f"<hr style='border: 1px solid #334155; margin: 16px 0;'>"
                f"<p style='color: #cbd5e1; font-size: 16px; line-height: 1.6;'>{page.content}</p>"
            )
            self.stacked.addWidget(browser)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stacked)
        self.setLayout(layout)
