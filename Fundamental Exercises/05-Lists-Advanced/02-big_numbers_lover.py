numbers = input().split()
numbers.sort(reverse=True)
for el in numbers:
    print(f'{el}', end='')
