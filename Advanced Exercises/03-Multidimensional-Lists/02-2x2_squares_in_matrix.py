rows, cols = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for el in range(rows)]
squares = []
count = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        square = [
            matrix[i][j:j+2],
            matrix[i + 1][j:j+2]
        ]
        squares.append(square)
for i in range(len(squares)):
    if squares[i][0] == squares[i][1]:
        count += 1
print(count)
