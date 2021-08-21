n = int(input())
plants = {}
for _ in range(n):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    if plant in plants:
        plants[plant]["Rarity"] = rarity
    plants[plant] = {"Rarity": rarity, "Rating": []}
line = input()
while not line == "Exhibition":
    data = line.split(": ")
    command = data[0]
    args = data[1].split(" - ")
    if command == "Rate":
        plant = args[0]
        rating = int(args[1])
        if plant in plants:
            plants[plant]["Rating"].append(rating)
        else:
            print("error")
    elif command == "Update":
        plant = args[0]
        new_rarity = int(args[1])
        if plant in plants:
            plants[plant]["Rarity"] = new_rarity
        else:
            print("error")
    elif command == "Reset":
        plant = args[0]
        if plant in plants:
            plants[plant]["Rating"].clear()
        else:
            print("error")
    else:
        print("error")
    line = input()
result = {}
for key in plants:
    result[key] = {0: 0, 1: 0}
for key, value in plants.items():
    result[key][0] = value["Rarity"]
    if len(value["Rating"]) == 0:
        result[key][1] = 0
    else:
        result[key][1] = sum(value["Rating"])/len(value["Rating"])

result = dict(sorted(result.items(), key=lambda el: (-el[1][0], -el[1][1])))
print("Plants for the exhibition:")
for key, value in result.items():
    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
