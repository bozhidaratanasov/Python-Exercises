category_item = {key: [] for key in input().split(", ")}
total_quantity = 0
total_quality = 0
n = int(input())
for _ in range(n):
    data = input().split(" - ")
    category = data[0]
    item = data[1]
    quality_and_quantity = data[2].split(";")
    quantity = int(quality_and_quantity[0][quality_and_quantity[0].find(':') + 1:])
    quality = int(quality_and_quantity[1][quality_and_quantity[1].find(':') + 1:])
    category_item[category].append(item)
    total_quantity += quantity
    total_quality += quality
print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality / len(category_item):.2f}")
for key, value in category_item.items():
    print(f"{key} -> {', '.join(value)}")
