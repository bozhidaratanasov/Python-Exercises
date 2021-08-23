positive = []
negative = []
even = []
odd = []
for el in input().split(", "):
    if int(el) >= 0:
        positive.append(el)
    if int(el) < 0:
        negative.append(el)
    if int(el) % 2 == 0:
        even.append(el)
    if int(el) % 2 == 1:
        odd.append(el)
print("Positive: " + ', '.join(positive))
print("Negative: " + ', '.join(negative))
print("Even: " + ', '.join(even))
print("Odd: " + ', '.join(odd))
