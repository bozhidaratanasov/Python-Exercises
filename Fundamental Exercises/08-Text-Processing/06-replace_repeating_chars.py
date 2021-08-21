string = input()
chars = []
for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        continue
    chars.append(string[i])
    if i == len(string) - 2:
        chars.append(string[i+1])
print("".join(chars))
