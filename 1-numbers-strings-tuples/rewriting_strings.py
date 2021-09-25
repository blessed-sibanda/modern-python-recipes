from string import whitespace, punctuation

title = "Recipe 5: Rewriting, and the Immutable String"

"""
We want to perform the followinh
- remove the part up to the ':'
- replace the punctuation with '_' & make all characters lowercase
"""

# Slicing
colon_position = title.index(':')

discard, post_colon = title[:colon_position], title[colon_position+1:]
print(discard)
print(post_colon)

# partition() method
pre_colon_text, _, post_colon_text = title.partition(':')
print('Pre colon text ==>', pre_colon_text)
print('Post colon text ==>', post_colon_text)

# Replacing all punctuation characters and whitespace with an underscore

# using replace() method
for character in whitespace+punctuation:
    post_colon_text = post_colon_text.replace(character, '_')

print('Processed post colon text')
print(post_colon_text)

# using translate() method
print('Result of using translate method')
title = "Recipe 5: Rewriting an Immutable String"
result = title.translate({ord(c): '_' for c in whitespace+punctuation})
print(result)

print("Removing extra punctuation marks")
print('Before ==>', post_colon_text)
post_colon_text = post_colon_text.strip('_')
print("After ==>",post_colon_text)

print("Replacing multiple underscores with one underscore")
print('Before ==>', post_colon_text)
while '__' in post_colon_text:
    post_colon_text = post_colon_text.replace('__', '_')
print("After ==>",post_colon_text)
