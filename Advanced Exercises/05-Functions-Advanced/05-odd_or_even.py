def odd_or_even(command, numbers):
    if command == "Odd":
        result = sum([el for el in numbers if el % 2 == 1]) * len(numbers)
        print(result)
    elif command == "Even":
        result = sum([el for el in numbers if el % 2 == 0]) * len(numbers)
        print(result)


command = input()
numbers = [int(el) for el in input().split()]
odd_or_even(command, numbers)
