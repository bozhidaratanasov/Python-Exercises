def palindrome_integers(string: str):
    numbers = string.split(', ')
    counter = 0
    for element in numbers:
        for index in range (len(element)):
            if element[index] == element[len(element) - index - 1]:
                counter += 1
            continue
        if counter == len(element):
            print('True')
        else:
            print('False')
        counter = 0


string1 = input()
palindrome_integers(string1)
