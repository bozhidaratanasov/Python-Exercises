from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    best_pureness = 0
    current_pureness = 0
    best_rotation = 0

    for i in range(k):
        numbers.rotate(1)
        for j in range(len(numbers)):
            current_pureness += numbers[j] * j
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = i + 1
        current_pureness = 0

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


print(best_list_pureness([7, 9, 2, 5, 3, 4], 3))
