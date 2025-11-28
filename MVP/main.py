from model.repository import ItemRepository
from presenter.item_presenter import ItemPresenter
from view.console_view import ConsoleView

repo = ItemRepository()
view = ConsoleView()
presenter = ItemPresenter(repo, view)

presenter.add_item("Laptop")
presenter.add_item("Tablet")
presenter.add_item("Keyboard")
