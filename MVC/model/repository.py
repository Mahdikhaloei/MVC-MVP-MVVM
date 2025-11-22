"""
Repository module for managing Item entities in the MVC architecture.
"""

import logging
from model.entities import Item
from typing import List, Optional


class ItemRepository:
    def __init__(self):
        self._items: List[Item] = []
        self._id_counter = 1

    def add_item(self, name: str) -> Item:
        item = Item(self._id_counter, name)
        self._items.append(item)
        self._id_counter += 1
        logging.info(f"Item added: {item.id} - {item.name}")
        return item

    def get_item(self, _id: int) -> Optional[Item]:
        for item in self._items:
            if item.id == _id:
                return item
        logging.warning(f"Item with id {_id} not found.")
        return None

    def get_all_items(self) -> List[Item]:
        return self._items
