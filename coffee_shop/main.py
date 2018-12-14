from coffee_shop.base import BASE
from coffee_shop.ingredients import INGREDIENTS
from coffee_shop.drink import DRINK


drink1 = DRINK()
base1 = BASE("tea")
ingredients1 = INGREDIENTS("milk")
ingredients2 = INGREDIENTS("sugar")

print(base1.price())

drink1.print_total()
drink1.print_contents()