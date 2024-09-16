number=int(input())

for _ in range(number):
    command=int(input())
    if command % 2 != 0:
        print(f'{command} is odd!')
        break
else:
    print('All numbers are even.')
