from collections import deque
n = int(input())
pumps = deque()

for _ in range(n):
    pump = [int(el) for el in input().split()]
    pumps.append(pump)

for i in range(n):
    is_Valid = True
    fuel = 0
    for _ in range(n):
        current = pumps.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_Valid = False
        pumps.append(current)
    if is_Valid:
        print(i)
        break
    pumps.append(pumps.popleft())
