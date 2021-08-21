numbers = [int(el) for el in input().split(', ')]
boundary = 0
while not numbers == []:
    boundary += 10
    print(f'Group of {boundary}\'s: {list(filter(lambda el: el <= boundary, numbers))}')
    numbers = [el for el in numbers if el > boundary]
