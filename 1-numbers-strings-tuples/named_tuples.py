from typing import NamedTuple
from fractions import Fraction


class Ingredient(NamedTuple):
    ingredient: str
    amount: str
    unit: str


item_2 = Ingredient('Kumquat', '2', 'cups')
a = Fraction(item_2.amount)
print(a)

b = f"Use {item_2.amount} {item_2.unit} fresh {item_2.ingredient}"
print(b)


class IngredientF(NamedTuple):
    ingredient: str
    amount: Fraction
    unit: str


item_3 = IngredientF('Kumquat', Fraction('2'), 'cups')
c = f'{item_3.ingredient} doubled: {item_3.amount * 2}'
print(c)
