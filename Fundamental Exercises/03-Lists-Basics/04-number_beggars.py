numbers = input().split(', ')
beggars_count = int(input())
sums = []
beggars = []
index = 0
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for beggar in range(beggars_count):
    beggars.append(0)

for number in numbers:
    beggars[index] += number
    index += 1

    if index == beggars_count:
        index = 0
print(beggars)