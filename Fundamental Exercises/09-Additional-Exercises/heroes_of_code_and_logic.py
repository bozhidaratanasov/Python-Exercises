n = int(input())
heroes_hp = {}
heroes_mp = {}
for index in range(0, n):
    args = input().split()
    hero = args[0]
    hp = int(args[1])
    mp = int(args[2])
    heroes_hp[hero] = hp
    heroes_mp[hero] = mp
line = input()
while not line == "End":
    args = line.split(" - ")
    command = args[0]
    if command == "CastSpell":
        hero = args[1]
        mp_needed = int(args[2])
        spell_name = args[3]
        if heroes_mp[hero] >= mp_needed:
            heroes_mp[hero] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_mp[hero]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        hero = args[1]
        damage = int(args[2])
        attacker = args[3]
        heroes_hp[hero] -= damage
        if heroes_hp[hero] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_hp[hero]} HP left!")
        else:
            heroes_hp.pop(hero)
            heroes_mp.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif command == "Recharge":
        hero = args[1]
        amount = int(args[2])
        if heroes_mp[hero] + amount > 200:
            amount = 200 - heroes_mp[hero]
        heroes_mp[hero] += amount
        print(f"{hero} recharged for {amount} MP!")
    elif command == "Heal":
        hero = args[1]
        amount = int(args[2])
        if heroes_hp[hero] + amount > 100:
            amount = 100 - heroes_hp[hero]
        heroes_hp[hero] += amount
        print(f"{hero} healed for {amount} HP!")
    line = input()

heroes_hp = dict(sorted(heroes_hp.items(), key=lambda el: (-el[1], el[0])))
for key in heroes_hp:
    print(f"{key}")
    print(f"  HP: {heroes_hp[key]}")
    print(f"  MP: {heroes_mp[key]}")
