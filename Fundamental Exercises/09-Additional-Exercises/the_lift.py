people_count = int(input())
lift_cabins = [int(el) for el in input().split(' ')]
for index in range(len(lift_cabins)):
    if people_count < 4:
        lift_cabins[index] += people_count
        people_count = 0
    elif lift_cabins[index] <= 4:
        people_count -= (4 - lift_cabins[index])
        lift_cabins[index] += (4 - lift_cabins[index])
result = ' '.join([str(el) for el in lift_cabins])
if people_count > 0:
    print(f'There isn\'t enough space! {people_count} people in a queue!\n'
          f'{result}')
else:
    print(f'The lift has empty spots!\n'
          f'{result}')
