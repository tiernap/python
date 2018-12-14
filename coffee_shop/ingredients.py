from coffee_shop.drink import DRINK


class INGREDIENTS(DRINK):
    def __init__(self, type):
        self.type = type
        self.price_list = {'milk': 0.5, 'sugar': 0.5, 'syrup': 1}
        DRINK.total += self.price_list[self.type]
        DRINK.contents.append(self.type)

    def price(self):
        return self.price_list[self.type]

