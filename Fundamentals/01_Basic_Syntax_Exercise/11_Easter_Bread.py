one_loaf_eggs = 1
one_loaf_flour = 1000
one_loaf_milk = 0.25

one_liter_milk = one_loaf_milk * 4

budget = float(input())
price_kilo_flour = float(input())
price_eggs = price_kilo_flour * 0.75
price_kilo_milk = price_kilo_flour + (price_kilo_flour * 0.25)

count_loaf = 0
count_colored_eggs = 0
one_loaf = one_loaf_eggs + one_loaf_flour + one_loaf_milk
price_one_loaf = price_eggs + price_kilo_flour + (price_kilo_milk / 4)

while budget > price_one_loaf:
    count_colored_eggs += 3
    count_loaf += 1
    budget -= price_one_loaf
    if count_loaf % 3 == 0:
        count_colored_eggs -= (count_loaf - 2)
print(f'You made {count_loaf} loaves of Easter bread! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.')
