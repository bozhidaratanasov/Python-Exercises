# Solution 1
n = int(input())
names = []
for _ in range(n):
    name = input()
    if name in names:
        continue
    names.append(name)
print("\n".join(names))

# Solution 2
n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)
print("\n".join(list(set(names))))

