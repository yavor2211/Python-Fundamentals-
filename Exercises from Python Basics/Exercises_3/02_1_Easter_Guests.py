import math

THRESHOLD_TWO = 2
SWEETBREAD_PRICE = 4  # 1 sweetbread is enough for 3
EGG_PRICE = 0.45  # 1 guest  gets 2 eggs

amount_guests = int(input())
budget = int(input())
result = ''

amount_eggs = amount_guests * THRESHOLD_TWO
prices_total_eggs = amount_eggs * EGG_PRICE
amount_sweetbread = math.ceil(amount_guests / 3)
price_sweetbread = amount_sweetbread * SWEETBREAD_PRICE

total_price = price_sweetbread + prices_total_eggs

if budget >= total_price:
    result += f'Lyubo bought {amount_sweetbread} Easter bread and {amount_eggs} eggs.\n'
    result += f'He has {budget - total_price:.2f} lv. left.'
else:
    result += f"Lyubo doesn't have enough money.\n"
    result += f'He needs {total_price - budget:.2f} lv. more.'

print(result)
