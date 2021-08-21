numbers = input().split()
result = ""
while len(numbers) > 0:
    result = result + numbers.pop() + " "
print(result)
