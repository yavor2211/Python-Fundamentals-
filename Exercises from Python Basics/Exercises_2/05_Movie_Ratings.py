movie_count = int(input())

best_movie_name = ''
best_movie_rating = -10

worst_movie_name = ''
worst_movie_rating = 10

average_rating = 0

for movie in range(movie_count):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > best_movie_rating:
        best_movie_rating = movie_rating
        best_movie_name = movie_name
    elif movie_rating < worst_movie_rating:
        worst_movie_name = movie_name
        worst_movie_rating = movie_rating

    average_rating += movie_rating
print(f'{best_movie_name} is with highest rating: {best_movie_rating:.1f}')
print(f'{worst_movie_name} is with lowest rating: {worst_movie_rating:.1f}')
print(f'Average rating: {average_rating / movie_count:.1f}')
