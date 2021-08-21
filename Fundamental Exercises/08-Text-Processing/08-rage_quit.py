string = input()
chars = []
unique_list = []
for el in string:
    if not el.isdigit():
        chars.append(el)
        unique_list.append(el.upper())
        continue
    string = string.replace(''.join(chars), (''.join(chars) * int(el)).upper())
    string = string.replace(el, "")
    chars.clear()
unique_count = len(set(unique_list))
print(f"Unique symbols used: {unique_count}")
print(string)
