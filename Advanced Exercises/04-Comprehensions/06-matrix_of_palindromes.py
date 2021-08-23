import string
letters = string.ascii_lowercase
rows, cols = [int(el) for el in input().split()]
matrix = [[letters[row] + letters[i+row] + letters[row] for i in range(cols)] for row in range(rows)]
for el in matrix:
    print(" ".join(el))
