size_eggs = input()
color_eggs = input()
amount_eggs = int(input())

THRESHOLD_PERCENTAGE = 0.35
result = ''
price = 0

if size_eggs == 'Large':
    if color_eggs == 'Red':
        price += 16
    elif color_eggs == 'Green':
        price += 12
    elif color_eggs == 'Yellow':
        price += 9

elif size_eggs == 'Medium':
    if color_eggs == 'Red':
        price += 13
    elif color_eggs == 'Green':
        price += 9
    elif color_eggs == 'Yellow':
        price += 7
elif size_eggs == 'Small':
    if color_eggs == 'Red':
        price += 9
    elif color_eggs == 'Green':
        price += 8
    elif color_eggs == 'Yellow':
        price += 5

price_eggs = price * amount_eggs
expenses = price_eggs * THRESHOLD_PERCENTAGE
total_price = price_eggs - expenses

result += f'{total_price:.2f} leva.'
print(result)
