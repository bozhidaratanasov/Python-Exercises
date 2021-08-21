def password_validator(password: str):
    counter = 0
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for el in password:
        if el.isdigit():
            counter += 1
        if not el.isdigit() and not el.isalpha():
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print('Password is valid')


pass1 = input()
password_validator(pass1)
