string = input()
languages = {}
users = {}
while not string == 'exam finished':
    args = string.split('-')
    username = args[0]
    if len(args) == 3:
        language = args[1]
        points = args[2]
        points = int(points)
        if language not in languages:
            languages[language] = []
        languages[language].append(username)
        if username not in users:
            users[username] = points
    elif args[1] == 'banned':
        users.pop(username)

    string = input()

users = dict(sorted(users.items(), key=lambda el: (-el[1], el[0])))
languages = dict(sorted(languages.items(), key=lambda el: (-len(el[1]), el[0])))
print('Results:')
for key, value in users.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in languages.items():
    print(f'{key} - {len(value)}')
