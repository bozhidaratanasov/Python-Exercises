from collections import deque
cups = deque([int(el) for el in input().split()])
bottles = deque([int(el) for el in input().split()])
wasted_litters = 0
while cups and bottles:
    if cups[0] <= bottles[-1]:
        wasted_litters += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()
    elif cups[0] > bottles[-1]:
        while True:
            if bottles[-1] >= cups[0]:
                wasted_litters += bottles[-1] - cups[0]
                cups.popleft()
                bottles.pop()
                break
            else:
                cups[0] -= bottles[-1]
                bottles.pop()
if not cups:
    result = ""
    while bottles:
        result += str(bottles.pop()) + " "
    print(f"Bottles: {result}")
elif cups:
    result = ""
    while cups:
        result += str(cups.popleft()) + " "
    print(f"Cups: {result}")
print(f"Wasted litters of water: {wasted_litters}")

