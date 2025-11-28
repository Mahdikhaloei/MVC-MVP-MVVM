"""ViewModel for managing items in MVVM architecture."""

from typing import List
from model.repository import ItemRepository


class ItemViewModel:
    def __init__(self, repo: ItemRepository):
        self.repo = repo
        self.items: List[str] = []

    def load_items(self) -> None:
        self.items = [f"{i.id}: {i.name}" for i in self.repo.get_all()]

    def add_item(self, name: str) -> None:
        self.repo.add(name)
        self.load_items()
