amount_eggs_beginning = int(input())
command = input()
counter = 0
result = ''
while command != "Close":
    count_eggs = int(input())
    if command == "Buy":
        if amount_eggs_beginning < count_eggs:
            result += f"Not enough eggs in store!\n"
            result += f"You can buy only {amount_eggs_beginning}."
            break
        amount_eggs_beginning -= count_eggs
        counter += count_eggs
    elif command == "Fill":
        amount_eggs_beginning += count_eggs
    command = input()
else:
    result += "Store is closed!\n"
    result += f"{counter} eggs sold."

print(result)
