def smallest_number(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    return num3


a = int(input())
b = int(input())
c = int(input())
result = smallest_number(a, b, c)
print(result)
