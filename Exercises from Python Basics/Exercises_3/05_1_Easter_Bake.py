import math
import sys

one_packet_flour = 750
one_packet_sugar = 950
count_sugar = 0
count_flour = 0
packages_sugar = 0
packages_flour = 0
result = ''

maximum_flour = -sys.maxsize
maximum_sugar = -sys.maxsize

sweetbread = int(input())

for materials in range(sweetbread):
    amount_sugar = int(input())
    amount_flour = int(input())

    count_sugar += amount_sugar
    count_flour += amount_flour
    packages_sugar = math.ceil(count_sugar / one_packet_sugar)
    packages_flour = math.ceil(count_flour / one_packet_flour)

    if amount_sugar > maximum_sugar:
        maximum_sugar = amount_sugar
    if amount_flour > maximum_flour:
        maximum_flour = amount_flour

print(f'Sugar: {packages_sugar}\n'
      f'Flour: {packages_flour}\n'
      f'Max used flour is {maximum_flour} grams, max used sugar is {maximum_sugar} grams.')
