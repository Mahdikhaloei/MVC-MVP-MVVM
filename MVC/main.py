from model.repository import ItemRepository
from controller.item_controller import ItemController
from view.console_view import ConsoleView


repo = ItemRepository()
controller = ItemController(repo)
view = ConsoleView()

# Adding sample items
controller.create_item("Item 1")
controller.create_item("Item 2")
controller.create_item("Item 3")

# Listing all items
items = controller.list_items()
view.display_items(items)

# Getting an item by ID
item_id = 2
item = controller.get_item(item_id)
view.display_item(item)
