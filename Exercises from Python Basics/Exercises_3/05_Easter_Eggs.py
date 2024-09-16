count_painted_eggs = int(input())

count_red = 0
count_orange = 0
count_blue = 0
count_green = 0
total_count = 0
result = ''

for egg in range(count_painted_eggs):
    color_egg = input()
    if color_egg == 'red':
        count_red += 1
        total_count += 1
    elif color_egg == 'orange':
        count_orange += 1
        total_count += 1
    elif color_egg == 'blue':
        count_blue += 1
        total_count += 1
    elif color_egg == 'green':
        count_green += 1
        total_count += 1

    if count_red > count_orange and \
            count_red > count_green \
            and count_red > count_blue:
        result = f'Max eggs: {count_red} -> {"red"}'

    elif count_orange > count_red \
            and count_orange > count_blue \
            and count_orange > count_green:
        result = f'Max eggs: {count_orange} -> {"orange"}'
    elif count_green > count_red \
            and count_green > count_blue \
            and count_green > count_orange:
        result = f'Max eggs: {count_green} -> {"green"}'

    elif count_blue > count_red \
            and count_blue > count_green \
            and count_blue > count_orange:
        result = f'Max eggs: {count_blue} -> {"blue"}'

print(f'Red eggs: {count_red}\n'
      f'Orange eggs: {count_orange}\n'
      f'Blue eggs: {count_blue}\n'
      f'Green eggs: {count_green}\n'
      f'{result}')
