number = float(input())

if number == 0:
    print(f'zero')
elif number > 0:
    if number < 1:
        print(f'small positive')
    elif number > 1_000_000:
        print(f'large positive')
    else:
        print(f'positive')
else:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1_000_000:
        print('large negative')
    else:
        print('negative')
