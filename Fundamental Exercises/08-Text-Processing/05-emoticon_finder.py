string = input()
result = []
for index in range(len(string)):
    if string[index] == ':':
        result.append(string[index] + string[index + 1])
for el in result:
    print(el)
