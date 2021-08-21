n = int(input())
stack = []
for _ in range(n):
    data = input().split()
    query = data[0]
    if query == "1":
        stack.append(int(data[1]))
    elif query == "2":
        if not stack:
            continue
        stack.pop()
    elif query == "3":
        print(max(stack))
    elif query == "4":
        print(min(stack))
stack = [str(el) for el in stack]
print(", ".join(reversed(stack)))
