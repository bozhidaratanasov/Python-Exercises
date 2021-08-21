open_list = ["[","{","("]
close_list = ["]","}",")"]
sequence = input()
stack = []
for el in sequence:
    if el in open_list:
        stack.append(el)
    elif el in close_list:
        pos = close_list.index(el)
        if open_list[pos] == stack[-1] and stack:
            stack.pop()
if not stack:
    print("YES")
else:
    print("NO")
