num = int(input())
a_letter_ascii = ord('a')
for n in range(a_letter_ascii, a_letter_ascii + num):
    for k in range(a_letter_ascii, a_letter_ascii + num):
        for j in range(a_letter_ascii, a_letter_ascii + num):
            print(f'{chr(n)}{chr(k)}{chr(j)}')