from collections import deque
green_light = int(input())
free_window = int(input())
total_duration = green_light + free_window
characters = deque()
count_of_cars = 0
crash_happened = False
green_ended = False
command = input()
while not command == "End":
    if command == "green":
        total_duration = green_light + free_window
    else:
        for el in command:
            characters.append(el)
        for _ in range(len(characters) + 1):
            if total_duration == 0:
                print("A crash happened!")
                print(f"{command} was hit at {characters.popleft()}.")
                crash_happened = True
                break
            if not characters:
                count_of_cars += 1
                continue
            if total_duration <= free_window:
                green_ended = True
            characters.popleft()
            total_duration -= 1
        if crash_happened or green_ended:
            break
    command = input()
if not crash_happened:
    print("Everyone is safe.")
    print(f"{count_of_cars} total cars passed the crossroads.")

