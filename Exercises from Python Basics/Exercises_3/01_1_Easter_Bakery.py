THRESHOLD_TWENTY_FIVE = 0.25
THRESHOLD_TEN = 0.10
THRESHOLD_EIGHTY = 0.80

price_flour = float(input())
kilograms_flour = float(input())
kilograms_sugar = float(input())
eggs = int(input())
yeast = int(input())

price_sugar = price_flour - (price_flour * THRESHOLD_TWENTY_FIVE)
price_eggs = price_flour + (price_flour * THRESHOLD_TEN)
price_yeast = price_sugar - (price_sugar * THRESHOLD_EIGHTY)

total_price = (price_yeast*yeast) + (price_eggs*eggs) + (price_sugar*kilograms_sugar) + (price_flour*kilograms_flour)

print(f'{total_price:.2f}')
