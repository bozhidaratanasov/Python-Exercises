def parse_to_char(word):
    temp = ''
    for char in word:
        if not str(char).isdigit():
            break
        temp += char
    new_word = word.replace(temp, chr(int(temp)))
    return  new_word


def swap_letters(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return ''.join(temp)


def decrypt(word):
    res = parse_to_char(word)
    res = swap_letters(res)
    return res


secret_message = input().split()
decrypted_message = [decrypt(word) for word in secret_message]
print(' '.join(decrypted_message))
