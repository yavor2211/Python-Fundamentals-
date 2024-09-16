amount_sweetbread = int(input())

top_score = 0
best_chef = ''

for _ in range(amount_sweetbread):
    new_best_baker = False
    score = 0
    name = input()

    while True:
        command = input()
        if command == 'Stop':
            break

        score += int(command)
        if score > top_score:
            top_score = score
            best_chef = name
            new_best_baker = True
    print(f'{name} has {score} points.')
    if new_best_baker:
        print(f'{best_chef} is the new number 1!')

print(f'{best_chef} won competition with {top_score} points!')
