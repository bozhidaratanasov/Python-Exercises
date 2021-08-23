def even_numbers(numbers):
    print(list(filter(lambda el: el % 2 == 0, numbers)))
    return


numbers = [int(el) for el in input().split()]
even_numbers(numbers)
