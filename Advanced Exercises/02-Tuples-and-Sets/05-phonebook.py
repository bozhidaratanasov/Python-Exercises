person_number = {}
line = input()
while "-" in line:
    data = line.split("-")
    name = data[0]
    number = data[1]
    person_number[name] = number
    line = input()
for _ in range(int(line)):
    name = input()
    if name not in person_number:
        print(f"Contact {name} does not exist.")
        continue
    print(f"{name} -> {person_number[name]}")
