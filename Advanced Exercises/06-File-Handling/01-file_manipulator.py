import io
import os
line = input()
while not line == "End":
    data = line.split("-")
    command = data[0]
    if command == "Create":
        file_name = data[1]
        open(file_name, 'w')
    elif command == "Add":
        file_name = data[1]
        content = data[2]
        try:
            opened_file = open(file_name, 'a')
            opened_file.write(content + "\n")
            opened_file.close()
        except FileNotFoundError:
            created_file = open(file_name, 'w')
            created_file.write(content + "\n")
            created_file.close()
    elif command == "Replace":
        file_name = data[1]
        old_string = data[2]
        new_string = data[3]
        new_lines = []
        try:
            with open(file_name, 'r') as opened_file:
                for line in opened_file:
                    new_lines.append(line.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occured!")
        try:
            with open(file_name, 'w') as opened_file:
                for line in new_lines:
                    opened_file.write(line)
        except FileNotFoundError:
            print("An error occured!")
    elif command == "Delete":
        pass
    line = input()
