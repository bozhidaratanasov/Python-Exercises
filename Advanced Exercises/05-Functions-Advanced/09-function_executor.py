def func_executor(*args):
    result = []
    for el in args:
        result.append(el[0](el[1][0], el[1][1]))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
