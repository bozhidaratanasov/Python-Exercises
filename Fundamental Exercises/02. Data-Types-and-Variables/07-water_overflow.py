current_capacity = 0
n = int(input())
for iteration in range(1 , n + 1):
    liters = int(input())
    current_capacity += liters
    if current_capacity > 255:
        print('Insufficient capacity!')
        current_capacity -= liters

print(current_capacity)