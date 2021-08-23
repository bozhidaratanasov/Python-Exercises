from collections import deque
size = int(input())
commands = deque(input().split())
field = [[el for el in input().split()] for el in range(size)]
starting_coals = 0
collected_coals = 0
game_ended = False
row_index = 0
col_index = 0
for i in range(size):
    for j in range(size):
        if field[i][j] == 'c':
            starting_coals += 1
        elif field[i][j] == 's':
            row_index = i
            col_index = j
while commands:
    command = commands.popleft()
    if command == "up" and row_index - 1 >= 0:
        row_index = row_index - 1
    elif command == "down" and row_index + 1 < size:
        row_index = row_index + 1
    elif command == "left" and col_index - 1 >= 0:
        col_index = col_index - 1
    elif command == "right" and col_index + 1 < size:
        col_index = col_index + 1
    if field[row_index][col_index] == 'e':
        print(f"Game over! ({row_index}, {col_index})")
        game_ended = True
        break
    elif field[row_index][col_index] == 'c':
        collected_coals += 1
        field[row_index][col_index] = '*'
        if collected_coals == starting_coals:
            print(f"You collected all coals! ({row_index}, {col_index})")
            game_ended = True
if not game_ended:
    print(f"{starting_coals - collected_coals} coals left. ({row_index}, {col_index})")
