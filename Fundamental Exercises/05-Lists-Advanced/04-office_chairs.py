number_of_rooms = int(input())
total_free_chairs = 0
isEnoughChairsInEveryRoom = True
for i in range(1, number_of_rooms + 1):
    string = input()
    args = string.split(' ')
    value = int(args[1])
    chairs = len(args[0])
    if chairs > value:
        current_free_chairs = chairs - value
        total_free_chairs += current_free_chairs
    elif value > chairs:
        isEnoughChairsInEveryRoom = False
        print(f'{value - chairs} more chairs needed in room {i}')

if total_free_chairs > 0 and isEnoughChairsInEveryRoom:
    print(f'Game On, {total_free_chairs} free chairs left')
