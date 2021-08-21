initial_list = input().split('!')
input_string = input()
while not input_string == 'Go Shopping!':
    args = input_string.split()
    command = args[0]
    if command == "Urgent":
        item = args[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command == 'Unnecessary':
        item = args[1]
        if item in initial_list:
            initial_list.remove(item)
    elif command == 'Correct':
        oldItem = args[1]
        new_Item = args[2]
        if oldItem in initial_list:
            index = initial_list.index(oldItem)
            initial_list.remove(oldItem)
            initial_list.insert(index, new_Item)
    elif command == 'Rearrange':
        item = args[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

    input_string = input()

print(', '.join(initial_list))