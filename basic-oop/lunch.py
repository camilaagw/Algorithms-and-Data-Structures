class Lunch:

    prices = {"menu 1": "12.00", "menu 2": "13.40"}

    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1" or self.menu == "menu 2":
            print(f'Your choice: {self.menu}. Price: {self.prices[self.menu]}')
        else:
            print("Error in menu")


if __name__ == "__main__":
    Paul = Lunch("menu 1")
    Paul.menu_price()