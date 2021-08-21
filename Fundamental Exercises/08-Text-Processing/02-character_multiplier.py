two_strings = input().split()
min_length = min(len(two_strings[0]), len((two_strings[1])))
sum = 0
for index in range(min_length):
    sum += ord(two_strings[0][index]) * ord(two_strings[1][index])
if len(two_strings[0]) > len(two_strings[1]):
    for index in range(len(two_strings[0]) - len((two_strings[1]))):
        sum += ord(two_strings[0][len(two_strings[1]) + index])
elif len(two_strings[0]) < len(two_strings[1]):
    for index in range(len(two_strings[1]) - len((two_strings[0]))):
        sum += ord(two_strings[1][len(two_strings[0]) + index])

print(sum)
