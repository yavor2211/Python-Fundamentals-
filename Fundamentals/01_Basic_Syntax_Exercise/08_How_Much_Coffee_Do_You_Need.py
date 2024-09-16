command = input()
total_coffee = 0

while command != 'END':
    if command == 'coding':
        total_coffee += 1
    elif command == 'dog':
        total_coffee += 1
    elif command == 'cat':
        total_coffee += 1
    elif command == 'movie':
        total_coffee += 1
    elif command == 'CODING':
        total_coffee += 2
    elif command == 'DOG':
        total_coffee += 2
    elif command == 'CAT':
        total_coffee += 2
    elif command == 'MOVIE':
        total_coffee += 2

    # if total_coffee > 5:
    #     print('You need extra sleep')
    #     break

    command = input()
print(total_coffee) if total_coffee <=5 else print('You need extra sleep')