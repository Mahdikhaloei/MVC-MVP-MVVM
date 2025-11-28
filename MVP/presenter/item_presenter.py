"""Presenter component for the MVP architecture."""

from typing import List, Protocol
from model.repository import ItemRepository


class ViewInterface(Protocol):
    def render_list(self, items: List[str]) -> None:
        pass


class ItemPresenter:
    def __init__(self, repo: ItemRepository, view: ViewInterface):
        self.repo = repo
        self.view = view

    def add_item(self, name: str) -> None:
        self.repo.add(name)
        self.update_view()

    def update_view(self) -> None:
        items = [f"{i.id}: {i.name}" for i in self.repo.get_all()]
        self.view.render_list(items)
