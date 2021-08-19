day_events = input().split('|')
energy = 100
coins = 100
dayCompleted = True
for item in day_events:
    event, value = item.split('-')
    value = int(value)
    if event == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
            print(f"You gained {100 - current_energy} energy.")
        else:
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        energy -= 30
        if energy < 0:
            energy += 50
            dayCompleted = False
            print(f"You had to rest!")
        else:
            coins += value
            print(f"You earned {value} coins.")

    else:
        coins -= value
        if coins >= 0:
            print(f"You bought {event}.")
        else:
            dayCompleted = False
            print(f"Closed! Cannot afford {event}.")
            break

if dayCompleted:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")