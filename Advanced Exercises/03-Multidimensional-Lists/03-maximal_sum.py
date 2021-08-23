rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for el in range(rows)]
matrix_3by3 = []
max_sum = 0
current_sum = 0
max_index = 0
result = [0]
for i in range(rows - 2):
    for j in range(cols - 2):
        current = [
            matrix[i][j:j+3],
            matrix[i+1][j:j+3],
            matrix[i+2][j:j+3]
        ]
        matrix_3by3.append(current)
for el in matrix_3by3:
    current_sum = 0
    for el1 in el:
        current_sum += sum(el1)
    if current_sum >= max_sum:
        max_sum = current_sum
        result[0] = el
print(f"Sum = {max_sum}")
for el in result:
    for el1 in el:
        print(" ".join([str(element) for element in el1]))
