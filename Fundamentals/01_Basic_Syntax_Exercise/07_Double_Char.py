first_string = input()
while first_string != 'End':
    if first_string != 'SoftUni':
        for char in first_string:
            print(char * 2, end='')
        print()
    first_string = input()
