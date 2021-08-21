string = input()
result = []
for index in range(len(string)):
    ascii_number = ord(string[index])
    result.append(chr(ascii_number +3))
print(''.join(result))
