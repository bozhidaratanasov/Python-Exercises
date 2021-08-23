dictionary = {el: len(el) for el in input().split(", ")}
result = ""
for key, value in dictionary.items():
    result += key + " -> " + str(value) + ", "
print(result)
