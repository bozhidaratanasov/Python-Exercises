def characters_in_range(char1, char2):
    result = ' '
    val_1 = ord(char1)
    val_2 = ord(char2)
    for char in range(val_1 + 1, val_2):
        result += chr(char) + ' '
    return result


char1 = input()
char2 = input()
print(characters_in_range(char1, char2), end='')
