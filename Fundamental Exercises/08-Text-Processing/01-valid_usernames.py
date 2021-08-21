usernames = input().split(', ')
usernames = [el for el in usernames if 3 < len(el) < 16]
for el in usernames:
    for char in el:
        if not char.isalnum() and not char == '-' and not char =='_':
            usernames.remove(el)
            break
for el in usernames:
    print(el)
