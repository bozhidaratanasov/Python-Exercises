def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(lambda el: el % 2 == 0, args[:-1]))
    return list(filter(lambda el: el % 2 == 1, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
