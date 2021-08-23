rows, cols = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for el in range(rows)]

line = input()
while not line == "END":
    data = line.split()
    command = data[0]
    if not len(data) == 5 or not command == "swap":
        print("Invalid input!")
        line = input()
        continue
    coordinate1_i = int(data[1])
    coordinate1_j = int(data[2])
    coordinate2_i = int(data[3])
    coordinate2_j = int(data[4])
    try:
        matrix[coordinate1_i][coordinate1_j], matrix[coordinate2_i][coordinate2_j] = matrix[coordinate2_i][coordinate2_j], matrix[coordinate1_i][coordinate1_j]
        for el in matrix:
            print(f" ".join([el1 for el1 in el]))
    except IndexError:
        print("Invalid input!")
    line = input()
