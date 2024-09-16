string_one = input()  # bubble gum
string_two = input()  # turtle hum
last_string=string_one
for character in range(len(string_one)):
    left_part = string_two[:character + 1]
    right_part = string_one[character + 1:]
    new_string=left_part+right_part
    if new_string != last_string:
        print(new_string)
        last_string=new_string

