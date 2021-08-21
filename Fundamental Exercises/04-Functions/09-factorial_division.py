def fac_division(number1, number2):
    fac1 = 1
    fac2 = 1
    for i in range(1, number1 + 1):
        fac1 *= i
    for i in range(1, number2 + 1):
        fac2 *= i
    result = fac1/fac2
    print(f'{result:.2f}')


num1 = int(input())
num2 = int(input())
fac_division(num1, num2)
