THRESHOLD_EIGHT = 8

voucher = int(input())
command = input()

count_movies = 0
count_purchases = 0

while voucher > 0:

    if command == 'End':
        break

    purchase = command
    movie_price = 0
    purchase_price = 0

    first_char = purchase[0]
    second_char = purchase[1]

    if len(purchase) > THRESHOLD_EIGHT:
        movie_price = ord(first_char) + ord(second_char)

        if voucher - movie_price < 0:
            break
        voucher -= movie_price
        count_movies += 1
    else:
        purchase_price = ord(first_char)

        if voucher - purchase_price < 0:
            break
        voucher -= purchase_price
        count_purchases += 1

    command = input()

print(f'{count_movies}\n{count_purchases}')
