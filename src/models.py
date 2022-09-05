from dataclasses import dataclass

@dataclass
class Page:
    name: str
    menu_name: str


@dataclass
class Section:
    name: str
    menu_name: str
    pages: list[Page]