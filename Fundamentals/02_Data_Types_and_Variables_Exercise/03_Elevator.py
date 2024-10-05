from math import ceil

number_of_people = int(input())
capacity = int(input())

total_courses = number_of_people / capacity

print(ceil(total_courses))
