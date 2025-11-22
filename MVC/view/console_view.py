"""
View module for the MVC architecture.
"""

from typing import List, Optional


class ConsoleView:
    def display_items(self, items: List[str]) -> None:
        for item in items:
            print(item)

    def display_item(self, item: Optional[str]) -> None:
        print(item if item else "not found")
