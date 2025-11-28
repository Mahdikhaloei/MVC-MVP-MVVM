"""Repository module for managing Item entities."""

from typing import List
import logging
from .entities import Item

logging.basicConfig(level=logging.INFO)


class ItemRepository:
    def __init__(self):
        self._items: List[Item] = []
        self._id_counter = 1

    def add(self, name: str) -> Item:
        item = Item(self._id_counter, name)
        self._items.append(item)
        self._id_counter += 1
        logging.info(f"created item {item.id}")
        return item

    def get_all(self) -> List[Item]:
        return self._items
