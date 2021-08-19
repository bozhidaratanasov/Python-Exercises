fire_data = input().split('#')
water_amount = int(input())
effort = 0
put_out_fires = []
for fire in fire_data:
    fire_type, value = fire.split(' = ')
    value = int(value)
    if fire_type == "High" and value not in range(81, 126):
        continue
    elif fire_type == "Medium" and value not in range(51, 81):
        continue
    elif fire_type == "Low" and value not in range(1, 51):
        continue
    if water_amount >=value:
        water_amount -= value
        effort += value * 0.25
        put_out_fires.append(value)
print("Cells:")
for fire in put_out_fires:
    print(f' - {fire}')
print(f'Effort:{effort: .2f}')
print(f'Total Fire: {sum(put_out_fires)}')