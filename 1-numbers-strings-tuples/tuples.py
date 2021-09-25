import re
from fractions import Fraction

ingredient = "Kumquat: 2 cups"
ingredient_pattern = re.compile(r'(?P<ingredient>\w+):\s+'
                                r'(?P<amount>\d+)\s+'
                                r'(?P<unit>\w+)')

match = ingredient_pattern.match(ingredient)

print(match.groups())


my_data = ('Rice', Fraction(1/4), 'cups')
print(my_data)

# We have to include an extra comma even when there's only one item in the tuple:
one_tuple = ('item',)
print(len(one_tuple))
print(one_tuple)

# extracting items from a tuple
print(my_data[1])
ingredient, amount, unit = my_data
print(ingredient)
print(amount)
print(ingredient)

t = ('Kumquat', '2', 'cups')
print(len(t))
print(t.count('2'))


if 'cups' in t:
    print(t.index('cups'))
