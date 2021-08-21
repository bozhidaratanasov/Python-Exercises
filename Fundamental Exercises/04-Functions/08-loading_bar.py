def loading_bar(number):
    progress = ['.'] * 10
    for i in range(number//10):
        progress[i] = '%'
    if number < 100:
        print(f'{number}% ', end='')
        print('[', end='')
        for el in progress:
            print(f'{el}', end='')
        print(']')

        print('Still loading...')
    elif number == 100:
        print('100% Complete!')
        print('[', end='')
        for el in progress:
            print(f'{el}', end= '')
        print(']')


num = int(input())
loading_bar(num)

