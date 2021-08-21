sequence = input().split()
command = input()
move = 1
while not command == 'end':
    index1, index2 = command.split()
    index1, index2 = int(index1), int(index2)
    if index1 == index2 or (index1 not in range(len(sequence)) or index2 not in range(len(sequence))):
        insert_position = len(sequence)//2
        inserted_el = f'-{move}a'
        sequence.insert(insert_position, inserted_el)
        sequence.insert(insert_position + 1, inserted_el)
        print('Invalid input! Adding additional elements to the board')
    elif sequence[index1] == sequence[index2]:
        print(f'Congrats! You have found matching elements - {sequence[index1]}!')
        sequence = [el for el in sequence if not el == sequence[index1]]

    else:
        print('Try again!')
    if len(sequence) == 0:
        break
    move += 1
    command = input()

if len(sequence) == 0:
    print(f'You have won in {move} turns!')

else:
    result = ' '.join(sequence)
    print(f'Sorry you lose :(\n{result}')
