amount_eggs_first = int(input())
amount_eggs_second = int(input())
winner = input()

counter_one = amount_eggs_first
counter_two = amount_eggs_second
result = ''

while True:
    if winner == 'one':
        counter_two -= 1
        if counter_two == 0:
            result += f'Player two is out of eggs. Player one has {counter_one} eggs left.'
            break
    elif winner == 'two':
        counter_one -= 1
        if counter_one == 0:
            result += f'Player one is out of eggs. Player two has {counter_two} eggs left.'
            break

    if winner == 'End':
        result += f'Player one has {counter_one} eggs left.\n'
        result += f'Player two has {counter_two} eggs left.'
        break
    winner = input()

print(result)
