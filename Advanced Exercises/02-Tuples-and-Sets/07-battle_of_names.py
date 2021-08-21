n = int(input())
even_numbers = set()
odd_numbers = set()
ascii_sum = 0
for index in range(1, n + 1):
    name = input()
    ascii_sum = 0
    for char in name:
        ascii_sum += ord(char)
    result = ascii_sum // index
    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)
if sum(even_numbers) == sum(odd_numbers):
    result = ", ".join([str(el) for el in odd_numbers | even_numbers])
    print(result)
elif sum(odd_numbers) > sum(even_numbers):
    result = ", ".join([str(el) for el in odd_numbers - even_numbers])
    print(result)
elif sum(odd_numbers) < sum(even_numbers):
    result = ", ".join([str(el) for el in odd_numbers ^ even_numbers])
    print(result)
