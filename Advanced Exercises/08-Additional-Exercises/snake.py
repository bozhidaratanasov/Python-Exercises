size = int(input())
snake_territory = [[el for el in input()] for el in range(size)]
row_index = 0
col_index = 0
food_quantity = 0
for i in range(size):
    for j in range(size):
        if snake_territory[i][j] == 'S':
            row_index = i
            col_index = j
command = input()
while True:
    snake_territory[row_index][col_index] = '.'
    if command == "up":
        row_index = row_index - 1
    elif command == "down":
        row_index = row_index + 1
    elif command == "left":
        col_index = col_index - 1
    elif command == "right":
        col_index = col_index + 1

    if food_quantity == 10:
        print("You won! You fed the snake.")
        snake_territory[row_index][col_index] = 'S'
        break
    elif row_index < 0 or row_index >= size or col_index < 0 or col_index >= size:
        print("Game over!")
        break

    if snake_territory[row_index][col_index] == "*":
        food_quantity += 1
    elif snake_territory[row_index][col_index] == "B":
        snake_territory[row_index][col_index] = "."
        for i in range(size):
            for j in range(size):
                if snake_territory[i][j] == 'B':
                    row_index = i
                    col_index = j
    snake_territory[row_index][col_index] = 'S'
    command = input()
print(f"Food eaten: {food_quantity}")
for el in snake_territory:
    print(''.join(el))
