data = [int(el) for el in input().split()]
n = data[0]
m = data[1]
set1 = set()
set2 = set()
for _ in range(n):
    number = int(input())
    set1.add(number)
for _ in range(m):
    number = int(input())
    set2.add(number)
for el in (set1 & set2):
    print(f"{el}")

