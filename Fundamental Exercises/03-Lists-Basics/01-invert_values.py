string = input()
numbers = string.split()
numbers = list(map(int, numbers))
numbers = [-i for i in numbers]
print(numbers)