from collections import deque
n = int(input())
matrix = [[int(el) for el in input().split()] for el in range(n)]
coordinates = deque([[int(el) for el in el.split(",")] for el in input().split()])
for i in range(n):
    for j in range(n):
        if i == coordinates[0][0] and j == coordinates[0][1]:
            coordinates.popleft()
            if i - 1 >= 0 and j - 1 >= 0:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if matrix[k][l] > 0 and (k != i or l != j) and not [k, l] in coordinates:
                            matrix[k][l] -= matrix[i][j]

            matrix[i][j] = 0
print(matrix)
while coordinates:
    coordinate1 = coordinates[0][0]
    coordinate2 = coordinates[0][1]
    coordinates.popleft()
    if coordinate1 - 1 >= 0 and coordinate2 - 1 >= 0:
        for i in range(coordinate1 - 1, coordinate1 + 2):
            for j in range(coordinate2 - 1, coordinate2 + 2):
                if matrix[i][j] > 0 and (i != coordinate1 or j != coordinate2) and not [i, j] in coordinates:
                    matrix[i][j] -= matrix[coordinate1][coordinate2]
        matrix[coordinate1][coordinate2] = 0
print(matrix)
