from collections import deque
bomb_effect = deque([int(el) for el in input().split(", ")])
bomb_casings = deque([int(el) for el in input().split(", ")])
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
pouch_count = 0
while True:
    pouch_count = 0
    if bomb_effect[0] + bomb_casings[-1] == 40:
        bombs["Datura Bombs"] += 1

    elif bomb_effect[0] + bomb_casings[-1] == 60:
        bombs["Cherry Bombs"] += 1

    elif bomb_effect[0] + bomb_casings[-1] == 120:
        bombs["Smoke Decoy Bombs"] += 1

    else:
        bomb_casings[-1] -= 5
        continue

    bomb_effect.popleft()
    bomb_casings.pop()

    for key, value in bombs.items():
        if value >= 3:
            pouch_count += 1
    if not bomb_effect or not bomb_casings or pouch_count == 3:
        break

if pouch_count == 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f"Bomb Effects: " + ', '.join(map(str, bomb_effect)))
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: " + ', '.join(map(str, bomb_casings)))
else:
    print("Bomb Casings: empty")
bombs = dict(sorted(bombs.items(), key=lambda el: el[0]))
for key, value in bombs.items():
    print(f"{key}: {value}")
