def exchange(num_list, index):
    if 0 <= index < len(num_list):
        first_half = num_list[: index + 1]
        second_half = num_list[index + 1:]
        exchanged_list = second_half + first_half
        return exchanged_list
    else:
        print('Invalid index')
        return num_list


def get_max_even_odd(num_list, num_type: str):
    odd_list = []
    even_list = []
    if num_type == 'odd':
        for el in num_list:
            if el % 2 == 1:
                odd_list.append(el)
            else:
                return 'No matches'
        max_odd = max(odd_list)
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == max_odd:
                return i
    elif num_type == 'even':
        for el in num_list:
            if el % 2 == 0:
                even_list.append(el)
        if len(even_list) == 0:
            return 'No matches'
        max_even = max(even_list)
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == max_even:
                return i


def get_min_even_odd(num_list, num_type: str):
    odd_list = []
    even_list = []
    if num_type == 'odd':
        for el in num_list:
            if el % 2 == 1:
                odd_list.append(el)
            else:
                return "No matches"
        min_odd = min(odd_list)
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == min_odd:
                return i
    elif num_type == 'even':
        for el in num_list:
            if el % 2 == 0:
                even_list.append(el)
        if len(even_list) == 0:
            return 'No matches'
        min_even = min(even_list)
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] == min_even:
                return i


string = input().split()
numbers = list(map(int, string))

command = input()
while not command == 'end':
    args = command.split()
    event = args[0]
    result = ''
    if event == 'exchange':
        index = int(args[1])
        numbers = exchange(numbers, index)
    elif event == 'max':
        result += str(get_max_even_odd(numbers, args[1]))
    elif event == 'min':
        result += str(get_min_even_odd(numbers, args[1]))

    command = input()
    print(result)
    