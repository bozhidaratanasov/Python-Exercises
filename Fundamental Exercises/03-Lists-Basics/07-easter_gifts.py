gifts = input().split()
command = ''
while not command == 'No Money':
    command = input()
    for string in command:
        args = command.split()
        if args[0] == "OutOfStock":
            for i in range(len(gifts)):
                if gifts[i] == args[1]:
                    gifts[i] = 'None'
        elif args[0] == "Required":
            index = int(args[2])
            if index < len(gifts):
                gifts[index] = args[1]
            else: continue
        elif args[0] == "JustInCase":
            gifts[-1] = args[1]
for el in gifts:
    if el == 'None':
        gifts.remove(el)
for el in gifts:
    print(f'{el} ', end='' )