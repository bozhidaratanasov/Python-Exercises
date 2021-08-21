message = input()
line = input()
while not line == "Decode":
    data = line.split("|")
    command = data[0]
    if command == "Move":
        number_of_letters = int(data[1])
        substring = message[:number_of_letters]
        message = message + substring
        message = message.replace(substring, "", 1)
    elif command == "Insert":
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    line = input()
print(f"The decrypted message is: {message}")
