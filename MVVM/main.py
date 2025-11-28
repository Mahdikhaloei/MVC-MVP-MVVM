"""Main application file for the MVVM pattern example."""

from model.repository import ItemRepository
from viewmodel.item_viewmodel import ItemViewModel
from view.console_view import ConsoleView

repo = ItemRepository()
vm = ItemViewModel(repo)
view = ConsoleView()

vm.add_item("Monitor")
vm.add_item("Keyboard")
vm.add_item("Headset")

view.render(vm.items)
