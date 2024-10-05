companions_count = int(input())
days = int(input())
total_coins = 0
for day in range(1,days+1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    if day % 3 == 0:
        total_coins -= 3 * companions_count
    if day % 5 == 0:
        total_coins += 20 * companions_count
        if day % 3 == 0:
            total_coins -= 2 * companions_count
    total_coins += 50
    total_coins -= 2 * companions_count

coins = total_coins // companions_count

print(f'{companions_count} companions received {coins} coins each.')
