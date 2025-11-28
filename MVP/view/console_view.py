"""Console view for displaying items in the MVP architecture."""

from typing import List


class ConsoleView:
    def render_list(self, items: List[str]) -> None:
        for i in items:
            print(i)
