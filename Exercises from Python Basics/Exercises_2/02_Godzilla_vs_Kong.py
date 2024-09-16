THRESHOLD_EXTRAS = 150
DISCOUNT_FOR_CLOTHING = 0.10
result = ''
movie_budget = float(input())
count_of_extras = int(input())
price_for_pair_clothing = float(input())

price_for_all_clothing = price_for_pair_clothing * count_of_extras
movie_decor = movie_budget * 0.10

if count_of_extras >= THRESHOLD_EXTRAS:
    price_for_all_clothing -= price_for_all_clothing * DISCOUNT_FOR_CLOTHING

total_price_movie = movie_decor + price_for_all_clothing

if total_price_movie > movie_budget:
    result = f'Not enough money!\nWingard needs {total_price_movie - movie_budget:.2f} leva more.'
else:
    result = f'Action!\nWingard starts filming with {movie_budget - total_price_movie:.2f} leva left. '

print(result)
