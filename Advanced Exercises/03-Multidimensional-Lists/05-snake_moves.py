from collections import  deque
rows, cols = [int(el) for el in input().split()]
snake = deque(list(input()))
for row in range(rows):
    s = ""
    for col in range(cols):
        piece = snake.popleft()
        s += piece
        snake.append(piece)
    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])
