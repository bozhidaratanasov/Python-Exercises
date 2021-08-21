n = int(input())
set1 = set()
set2 = set()
max_intersection = set()
for _ in range(n):
    set1.clear()
    set2.clear()
    data = input().split("-")
    first_start, first_end = data[0].split(",")[0:2]
    second_start, second_end = data[1].split(",")[0:2]
    for number in range(int(first_start), int(first_end) + 1):
        set1.add(number)
    for number in range(int(second_start), int(second_end) + 1):
        set2.add(number)
    if len(max_intersection) == 0:
        max_intersection = set1 & set2
    if len(set1 & set2) > len(max_intersection):
        max_intersection = set1 & set2
print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")
