"""
Controller for managing items in the MVC architecture.
"""

from typing import List, Optional
from model.repository import ItemRepository


class ItemController:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def create_item(self, name: str) -> None:
        self.repo.add_item(name)

    def list_items(self) -> List[str]:
        items = self.repo.get_all_items()
        return [f"{item.id}: {item.name}" for item in items]

    def get_item(self, id_: int) -> Optional[str]:
        item = self.repo.get_item(id_)
        if item:
            return f"{item.id}: {item.name}"
        return None
