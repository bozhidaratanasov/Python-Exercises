targets = [int(el) for el in input().split()]
string = input()
while not string == 'End':
    args = string.split()
    command = args[0]
    index = int(args[1])
    value = int(args[2])
    if command == 'Shoot':
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == 'Add':
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        if index - value >= 0 and index + value < len(targets):
            left_part = targets[:index - value]
            right_part = targets[index + value + 1:]
            targets = left_part + right_part

        else:
            print('Strike missed!')
    string = input()
targets = [str(el) for el in targets]
print('|'.join(targets))
