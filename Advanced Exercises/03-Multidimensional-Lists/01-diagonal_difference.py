size = int(input())
matrix = [[int(el) for el in input().split()] for el in range(size)]
diagonal_sum = 0
secondary_diagonal_sum = 0
for i in range(size):
    diagonal_sum += matrix[i][i]
for j in range(size):
    secondary_diagonal_sum += matrix[j][size - j - 1]
print(abs(diagonal_sum - secondary_diagonal_sum))
