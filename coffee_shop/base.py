from coffee_shop.drink import DRINK


class BASE(DRINK):
    def __init__(self, type):
        self.type = type
        self.price_list = {'robusta': 2, 'arabica': 2.5, 'tea': 2}
        DRINK.total += self.price_list[self.type]
        DRINK.contents.append(self.type)

    def price(self):
        return self.price_list[self.type]

