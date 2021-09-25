with open('some_file.txt', 'w', encoding='utf-8') as output:
    print('Discard \N{MAHJONG TILE RED DRAGON}', file=output)

with open('some_file.txt', 'r', encoding='utf-8') as input:
    text = input.read()

print(text)