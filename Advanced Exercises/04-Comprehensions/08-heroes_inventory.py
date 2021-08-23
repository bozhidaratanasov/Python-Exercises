hero_items = {key: [] for key in input().split(", ")}
hero_costs = {key: 0 for key in hero_items}
line = input()
while not line == "End":
    data = line.split("-")
    name = data[0]
    item = data[1]
    cost = int(data[2])
    if item not in hero_items[name]:
        hero_items[name].append(item)
        hero_costs[name] += cost
    line = input()
for key, value in hero_items.items():
    print(f"{key} -> Items: {len(value)}, Cost: {hero_costs[key]}")
