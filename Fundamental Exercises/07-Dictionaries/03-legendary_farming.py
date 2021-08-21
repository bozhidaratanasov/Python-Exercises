key_materials = {'motes': 0, 'shards': 0, 'fragments': 0}
legendary_item = {'motes': 'Dragonwrath', 'shards': 'Shadowmourne', 'fragments': 'Valanyr'}
junk = {}
obtained_material = ''
while obtained_material == '':
    args = input().lower().split()
    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                obtained_material = material
                key_materials[material] -= 250
                break
        else:
            junk[material] = 0
            junk[material] += quantity

print(f'{legendary_item[obtained_material]} obtained!')
key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junk = dict(sorted(junk.items()))
for key, value in key_materials.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')
