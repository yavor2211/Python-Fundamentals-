number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quality = 0

for current_snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_snowball = int(input())
    quality_snowball = int(input())
    value_snowball = (weight_of_snowball // time_snowball) ** quality_snowball
    if value_snowball > max_value:
        max_weight = weight_of_snowball
        max_time = time_snowball
        max_quality = quality_snowball
        max_value = value_snowball
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")

