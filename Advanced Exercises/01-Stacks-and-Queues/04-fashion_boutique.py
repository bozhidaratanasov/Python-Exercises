stack = [int(el) for el in input().split()]
rack_capacity = int(input())
rack_count = 1
sum_of_clothes = 0
while stack:
    sum_of_clothes += stack[-1]
    if sum_of_clothes < rack_capacity:
        stack.pop()
    elif sum_of_clothes == rack_capacity and stack:
        stack.pop()
        sum_of_clothes = 0
        rack_count += 1
    elif sum_of_clothes > rack_capacity:
        sum_of_clothes = 0
        rack_count += 1
print(rack_count)
