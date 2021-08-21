path = input().split('\\')
name_extension = path[-1].split('.')
print(f'File name: {name_extension[0]}')
print(f'File extension: {name_extension[1]}')
