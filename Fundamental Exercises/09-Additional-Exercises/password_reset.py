password = input()
string = input()
while not string == "Done":
    args = string.split(" ")
    command = args[0]
    if command == "TakeOdd":
        result = ""
        for index in range(1, len(password), 2):
            result += password[index]
        password = result
        print(password)
    elif command == "Cut":
        index = int(args[1])
        length = int(args[2])
        cut_string = password[index: index + length]
        password = password.replace(cut_string, "", 1)
        print(password)
    elif command == "Substitute":
        substring = args[1]
        substitute = args[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    string = input()
print(f"Your password is: {password}")
