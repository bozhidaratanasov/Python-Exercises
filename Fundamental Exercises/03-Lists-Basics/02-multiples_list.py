factor = int(input())
count = int(input())
lst = []
current_number = 0
for iteration in range(count):
    current_number += factor
    lst.append(current_number)

print(lst)