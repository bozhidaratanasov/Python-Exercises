inventory = input().split(', ')
command_string = input()
while not command_string == 'Craft!':
    args = command_string.split(' - ')
    command = args[0]
    items = args[1]
    if command == 'Collect':
        if items not in inventory:
            inventory.append(items)
    elif command == 'Drop':
        if items in inventory:
            inventory.remove(items)
    elif command == 'Combine Items':
        old_item, new_item = items.split(':')
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif command == 'Renew':
        if items in inventory:
            inventory.remove(items)
            inventory.append(items)
    command_string = input()
print(', '.join(inventory))
