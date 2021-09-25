from string import whitespace, punctuation

title = "Recipe 5: Rewriting an Immutable String"

title_list = list(title)

colon_position = title_list.index(':')

# delete the characters that are no longer needed
# lists are mutable
del title_list[:colon_position]

for position in range(len(title_list)):
    if title_list[position] in whitespace + punctuation:
        title_list[position] = '_'

title = ''.join(title_list)
print(title)
