def add_and_subtract(num1, num2, num3):
    def sum_numbers():
        result = num1 + num2
        return result

    def subtract():
        sum = sum_numbers()
        result = sum - num3
        return result

    return subtract()


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
