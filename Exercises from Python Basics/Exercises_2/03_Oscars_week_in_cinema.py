name_of_movie = input()
type_of_area = input()
amount_of_tickets_bought = int(input())

price_ticket = 0

if name_of_movie == 'A Star Is Born':
    if type_of_area == 'normal':
        price_ticket += 7.50
    elif type_of_area == 'luxury':
        price_ticket += 10.50
    elif type_of_area == 'ultra luxury':
        price_ticket += 13.50



elif name_of_movie == 'Bohemian Rhapsody':
    if type_of_area == 'normal':
        price_ticket += 7.35
    elif type_of_area == 'luxury':
        price_ticket += 9.45
    elif type_of_area == 'ultra luxury':
        price_ticket += 12.75

elif name_of_movie == 'Green Book':
    if type_of_area == 'normal':
        price_ticket += 8.15
    elif type_of_area == 'luxury':
        price_ticket += 10.25
    elif type_of_area == 'ultra luxury':
        price_ticket += 13.25

elif name_of_movie == 'The Favourite':
    if type_of_area == 'normal':
        price_ticket += 8.75
    elif type_of_area == 'luxury':
        price_ticket += 11.55
    elif type_of_area == 'ultra luxury':
        price_ticket += 13.95

total_price = price_ticket * amount_of_tickets_bought

print(f'{name_of_movie} -> {total_price:.2f} lv.')
