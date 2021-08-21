words = input().split(', ')
sequence = input()
result = [el for el in words if el in sequence]
print(result)
