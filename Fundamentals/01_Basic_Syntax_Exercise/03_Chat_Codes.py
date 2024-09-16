number_messages = int(input())
first_number = 88
second_number = 86
result = ''

for n in range(number_messages):
    number_lines = int(input())

    if number_lines == first_number:
        result += f'Hello\n'
    elif number_lines == second_number:
        result += f'How are you?\n'
    elif number_lines != first_number \
            and number_lines != second_number \
            and number_lines < first_number:
        result += f'GREAT!\n'
    elif number_lines > first_number:
        result += f'Bye.\n'

print(result)
