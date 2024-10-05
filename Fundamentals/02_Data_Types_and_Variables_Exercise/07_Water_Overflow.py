capacity = 255
total_water = 0
number = int(input())

for current_num in range(number):
    liters_of_water = int(input())
    if capacity - liters_of_water < 0:
        print(f'Insufficient capacity!')
        continue
    capacity -= liters_of_water
print(255 - capacity)
