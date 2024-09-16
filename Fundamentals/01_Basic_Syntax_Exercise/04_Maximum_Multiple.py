first_number=int(input()) # divisor - delim na nego
second_number=int(input())  # boundary - granicata do koqto delim
result=0

for number in range(second_number, first_number -1, -1):
    if number % first_number ==0:
        break

print(number)
