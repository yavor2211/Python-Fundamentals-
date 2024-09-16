count_student_tickets = 0
count_standard_tickets = 0
count_kid_tickets = 0

result = ''

while True:

    movie_name = input()

    if movie_name == 'Finish':
        break
    free_spaces = int(input())
    total_count_tickets = 0

    while free_spaces > total_count_tickets:
        ticket_type = input()
        if ticket_type == 'End':
            break

        if ticket_type == 'standard':
            count_standard_tickets += 1
        elif ticket_type == 'student':
            count_student_tickets += 1
        elif ticket_type == 'kid':
            count_kid_tickets += 1

        total_count_tickets += 1

    result += f'{movie_name} - {(total_count_tickets / free_spaces) * 100:.2f}% full.\n'
total_tickets = count_kid_tickets + count_student_tickets + count_standard_tickets
result += f'Total tickets: {total_tickets}\n' \
          f'{(count_student_tickets / total_tickets) * 100:.2f}% student tickets.\n' \
          f'{(count_standard_tickets / total_tickets) * 100:.2f}% standard tickets.\n' \
          f'{(count_kid_tickets / total_tickets) * 100:.2f}% kids tickets.'
print(result)
