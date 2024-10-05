starting_index = int(input())
last_index = int(input())
result = ''
for character in range(starting_index, last_index + 1):
    result = chr(character)
    if character == last_index:
        print(result)
    else:
        print(result, end=' ')
