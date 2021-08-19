integers = input().split()
n = int(input())
for i in range(len(integers)):
    integers[i] = int(integers[i])
for index in range(n):
    integers.remove(min(integers))
print(integers)