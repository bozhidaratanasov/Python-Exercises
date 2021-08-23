from collections import deque
rows, cols = [int(el) for el in input().split()]
lair = [[el for el in input()] for el in range(rows)]
commands = deque(input())
row_index = 0
col_index = 0
is_dead = False
for i in range(rows):
    for j in range(cols):
        if lair[i][j] == 'P':
            row_index = i
            col_index = j
while commands:
    command = commands.popleft()
    if command == "U" and row_index - 1 >= 0:
        row_index = row_index - 1
    elif command == "D" and row_index + 1 < rows:
        row_index = row_index + 1
    elif command == "L" and col_index - 1 >= 0:
        col_index = col_index - 1
    elif command == "R" and col_index + 1 < cols:
        col_index = col_index + 1
    else:
        print(f"won: {row_index} {col_index}")
        break
    if lair[row_index][col_index] == 'B':
        print(f"dead: {row_index} {col_index}")
    for i in range(rows - 1):
        for j in range(cols - 1):
            if lair[i][j] == 'B':
                if i - 1 >= 0 and j - 1 >= 0 or i + 1 < rows and j + 1 < cols:
                    if lair[i-1][j] == 'P':
                        is_dead = True
                    lair[i-1][j] = 'B'
                    if lair[i][j-1] == 'P':
                        is_dead = True
                    lair[i][j-1] = 'B'
                    if lair[i+1][j] == 'P':
                        is_dead = True
                    lair[i+1][j] = 'B'
                    if lair[i][j+1] == 'P':
                        is_dead = True
                    lair[i][j+1] = 'B'
    if is_dead:
        print(f"dead {row_index} {col_index}")
        break
