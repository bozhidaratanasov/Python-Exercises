neighbourhood = [int(el) for el in input().split('@')]
jump_command = input()
current_house = 0
counter = 0
while not jump_command == 'Love!':
    args = jump_command.split()
    length = int(args[1])
    current_house += length
    if current_house >= len(neighbourhood):
        current_house = 0
    neighbourhood[current_house] -= 2
    if neighbourhood[current_house] < 0:
        print(f'Place {current_house} already had Valentine\'s day.')
    if neighbourhood[current_house] == 0:
        print(f'Place {current_house} has Valentine\'s day.')

    jump_command = input()
print(f'Cupid\'s last position was {current_house}.')
for house in neighbourhood:
    if house > 0:
        counter += 1
if counter == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.')
