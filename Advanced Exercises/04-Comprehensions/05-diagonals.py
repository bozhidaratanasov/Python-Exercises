size = int(input())
matrix = [[int(el) for el in input().split(", ")] for el in range(size)]
primary_diagonal = []
secondary_diagonal = []
for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - i - 1])
res1 = ", ".join([str(el) for el in primary_diagonal])
res2 = ", ".join([str(el) for el in secondary_diagonal])
print(f"First diagonal: {res1}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {res2}. Sum: {sum(secondary_diagonal)}")
