from collections import deque
bullet_price = int(input())
gun_barrel = int(input())
bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())
empty_lock_or_bullets = False
while bullets and locks:
    for index in range(gun_barrel):
        if not locks or not bullets:
            empty_lock_or_bullets = True
            break
        if len(bullets) < gun_barrel:
            gun_barrel = len(bullets)
        if bullets[-1] <= locks[0]:
            bullets.pop()
            locks.popleft()
            intelligence_value -= bullet_price
            print("Bang!")
        elif bullets[-1] > locks[0]:
            bullets.pop()
            intelligence_value -= bullet_price
            print("Ping!")
    if empty_lock_or_bullets:
        break
    if bullets:
        print("Reloading!")
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
elif locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
