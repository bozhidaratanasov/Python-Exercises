size = int(input())
matrix = [[int(el) for el in input().split()] for el in range(size)]
line = input()
while not line == "END":
    data = line.split()
    command = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])
    if command == "Add":
        if row >= 0 and row < size and col >= 0 and col < size:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command == "Subtract":
        if row >= 0 and row < size and col >= 0 and col < size:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    line = input()
for el in matrix:
    print(*el)
