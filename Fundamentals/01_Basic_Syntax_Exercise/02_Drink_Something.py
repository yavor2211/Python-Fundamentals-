AGE_KIDS = 14
AGE_TEENS = 18
AGE_YOUNG_ADULT = 21
ADULT_AGE = 21

KIDS_DRINK = 'toddy'
TEENS_DRINK = 'coke'
YOUNG_ADULT_DRINK = 'beer'
ADULT_DRINK = 'whisky'

age = int(input())
result = ''

if age <= AGE_KIDS:
    result = f'drink {KIDS_DRINK}'
elif age <= AGE_TEENS:
    result = f'drink {TEENS_DRINK}'
elif age <= AGE_YOUNG_ADULT:
    result = f'drink {YOUNG_ADULT_DRINK}'
else:
    result = f'drink {ADULT_DRINK}'

print(result)
