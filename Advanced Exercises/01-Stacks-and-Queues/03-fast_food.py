from collections import deque
quantity = int(input())
queue = deque(int(el) for el in input().split())
print(max(queue))
while True:
    if queue[0] <= quantity:
        quantity -= queue.popleft()
        if not queue:
            break
    else:
        break
if not queue:
    print("Orders complete")
else:
    result = " ".join([str(el) for el in queue])
    print(f"Orders left: {result}")
