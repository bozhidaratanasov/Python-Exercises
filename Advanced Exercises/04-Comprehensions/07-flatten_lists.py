numbers = [[el for el in sequence if not el == " "] for sequence in input().split("|")]
result = ""
for i in range(len(numbers) - 1, -1, -1):
    for j in range(len(numbers[i])):
        result += numbers[i][j] + " "
print(result)
