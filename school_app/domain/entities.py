"""Domain entities representing application data.

Classes:
    Student: Information about a student displayed on the card.
    PageInfo: Title and HTML content for a page in the info panel.
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Represents a student card with personal and school information.

    Attributes:
        school: Name of the school. Defaults to placeholder.
        name: Student's full name. Defaults to placeholder.
        grade: Class/grade identifier. Defaults to placeholder.
        city: City where the school is located. Defaults to placeholder.
    """

    school: str = "________"
    name: str = "________"
    grade: str = "________"
    city: str = "________"


@dataclass
class PageInfo:
    """Represents a single page in the info panel.

    Attributes:
        title: Page heading displayed in blue.
        content: HTML-formatted body text.
    """

    title: str
    content: str
