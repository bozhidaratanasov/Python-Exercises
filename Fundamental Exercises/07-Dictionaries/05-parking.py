n = int(input())
users = {}
for _ in range(n):
    string = input()
    args = string.split()
    command = args[0]
    username = args[1]
    if command == 'register':
        if username not in users:
            users[username] = args[2]
            print(f'{username} registered {args[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {args[2]}')
    elif command == 'unregister':
        if username not in users:
            print(f'ERROR: user {username} not found')

        else:
            users.pop(username)
            print(f'{username} unregistered successfully')

for key, value in users.items():
    print(f'{key} => {value}')
