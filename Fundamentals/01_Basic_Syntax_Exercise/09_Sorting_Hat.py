threshold_five = 5
threshold_six = 6
command = input()
result = ''
while command != 'Welcome!':
    if command == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif len(command) < threshold_five:
        print(f'{command} goes to Gryffindor.')
    elif len(command) == threshold_five:
        print(f'{command} goes to Slytherin.')
    elif len(command) == threshold_six:
        print(f'{command} goes to Ravenclaw.')
    elif len(command) > threshold_six:
        print(f'{command} goes to Hufflepuff.')
    command = input()
if command == 'Welcome!':
    print('Welcome to Hogwarts.')
