from collections import deque
country_capital = {key:"" for key in input().split(", ")}
capitals = deque(input().split(", "))
for key in country_capital:
    print(f"{key} -> {capitals.popleft()}")
