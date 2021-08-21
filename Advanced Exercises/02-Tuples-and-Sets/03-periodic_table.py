n = int(input())
chemical_elements = set()
for _ in range(n):
    data = input().split()
    for el in data:
        chemical_elements.add(el)
for el in chemical_elements:
    print(el)
