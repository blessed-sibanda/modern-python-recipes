import re 

"""
Let's say that we want to decompose text from a recipe. Each line looks like this:

ingredient = "Kumquat: 2 cups"

We want to separate the ingredient from the measurements.
"""
ingredient = "Olive Oil: 200 mls"

ingredient_pattern = re.compile(
    r'(?P<ingrd>[\w\s]+):\s+' # name of the ingredient up to the ':'
    r'(?P<qty>\d+)\s+' # quantity, all digits up to a space
    r'(?P<unit>\w+)') # units, alphanumeric characters
match = ingredient_pattern.match(ingredient)
print(match)
print(match.groups())
print(match['ingrd'])
print(match['qty'])
print(match['unit'])