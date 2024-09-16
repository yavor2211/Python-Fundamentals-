init_eggs = int(input())
command = input()
bought_eggs = 0
while command != "Close":
    count_eggs = int(input())
    if command == "Buy":
        if init_eggs < count_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {init_eggs}.")
            break
        init_eggs = init_eggs - count_eggs
        bought_eggs += count_eggs
    elif command == "Fill":
        init_eggs = init_eggs + count_eggs
    command = input()
else:
    print("Store is closed!")
    print(f"{bought_eggs} eggs sold.")