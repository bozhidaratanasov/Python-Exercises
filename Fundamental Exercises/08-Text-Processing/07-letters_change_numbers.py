import string

sequences = input().split()
sum = 0
for el in sequences:
    number = int(el[1:len(el) - 1])
    first_position = string.ascii_lowercase.index(el[0].lower()) + 1
    last_position = string.ascii_lowercase.index(el[-1].lower()) + 1
    if el[0].isupper():
        number /= first_position
    elif el[0].islower():
        number *= first_position
    if el[-1].isupper():
        number -= last_position
    elif el[-1].islower():
        number += last_position
    sum += number
print(f"{sum:.2f}")