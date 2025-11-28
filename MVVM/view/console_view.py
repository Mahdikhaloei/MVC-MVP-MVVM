"""Console view for displaying items in the MVVM pattern."""


class ConsoleView:
    def render(self, items):
        for i in items:
            print(i)
