string = input()
result = {}
for el in string:
    if el == ' ':
        continue
    if el not in result:
        result[el] = 0

    result[el] += 1
for key, value in result.items():
    print(f'{key} -> {value}')
