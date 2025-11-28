"""
Model entities for the MVP architecture.
"""


class Item:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
