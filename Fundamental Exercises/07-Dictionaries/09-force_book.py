string = input()
force_sides = {}
while not string == 'Lumpawaroo':
    args = string.split()
    if '|' in args:
        force_user = ' '.join(args[args.index('|') + 1:])
        force_side = ' '.join(args[:args.index('|')])
        if force_user not in force_sides.values():
            force_sides[force_side] = []
        else:
            continue
        force_sides[force_side].append(force_user)
    elif '->' in args:
        force_user = ' '.join(args[:args.index('->')])
        force_side = ' '.join(args[args.index('->') + 1:])

        for value in force_sides.values():
            if force_user in value:
                value.remove(force_user)
        force_sides[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

    string = input()

force_sides = dict(sorted(force_sides.items(), key=lambda el: (-len(el[1]), el[0])))
for key, value in force_sides.items():
    if len(value) == 0:
        continue
    print(f'Side: {key}, Members: {len(value)}')
    for el in sorted(value):
        print(f'! {el}')
