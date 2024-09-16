rent_for_building = int(input())

statues_price = rent_for_building - (rent_for_building * 0.30)
catering_price = statues_price - (statues_price * 0.15)
sounding_price = catering_price / 2

total_price = rent_for_building + statues_price + catering_price + sounding_price

print(f'{total_price:.2f}')
