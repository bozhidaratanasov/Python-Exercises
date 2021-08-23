from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    if args[0] == "add":
        numbers_to_append = deque([int(el) for el in args[2:]])
        if args[1] == "beginning":
            while numbers_to_append:
                numbers.appendleft(numbers_to_append.pop())
        elif args[1] == "end":
            while numbers_to_append:
                numbers.append(numbers_to_append.popleft())
    elif args[0] == "remove":
        if args[1] == "beginning":
            if len(args) == 2:
                numbers.popleft()
            else:
                for i in range(int(args[2])):
                    numbers.popleft()
        elif args[1] == "end":
            if len(args) == 2:
                numbers.pop()
            else:
                for i in range(int(args[2])):
                    numbers.pop()
    return list(numbers)
