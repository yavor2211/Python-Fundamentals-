sweetbread_price=3.20
eggs_price=4.35 # for 12 eggs
cookies_price=5.40 # for kilogram
egg_paint_price=0.15 # per egg

count_sweetbread=int(input())
count_eggs=int(input())
kg_cookies=int(input())

total_price=(count_sweetbread*sweetbread_price)+(cookies_price*kg_cookies)+(count_eggs*eggs_price)
total_price_paint=(count_eggs*egg_paint_price)*12

total=f'{total_price+total_price_paint:.2f}'

print(total)