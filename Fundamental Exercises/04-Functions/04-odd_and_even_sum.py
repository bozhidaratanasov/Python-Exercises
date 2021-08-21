def sum_of_all_even_and_odd_numbers(num):
    even_sum = 0
    odd_sum = 0
    num = str(num)
    for el in num:
        el = int(el)
        if el % 2 == 0:
            even_sum += el
        else:
            odd_sum += el
    result = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return result


number = int(input())
print(sum_of_all_even_and_odd_numbers(number))
