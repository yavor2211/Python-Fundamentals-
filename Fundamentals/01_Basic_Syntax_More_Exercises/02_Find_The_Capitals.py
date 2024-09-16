one_string = input()

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = []

for character in range(0, len(one_string)):
    if one_string[character] in capital_letters:
        result.append(character)
print(result)
