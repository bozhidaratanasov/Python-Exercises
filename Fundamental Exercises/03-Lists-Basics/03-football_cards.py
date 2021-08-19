card = input().split()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
count_a = card.count('A')
count_b = card.count('B')
for iteration in range(count_a):
    A.pop()
for iteration in range(count_b):
    B.pop()
for string in card:
    team_name, number = string.split('-')
    number = int(number)
    if team_name == 'A':
        A.remove(number)
    if team_name == 'B':
        B.remove(number)
print(f'Team A - {len(A)}; Team B - {len(B)}')
if len(A) < 7 or len(B) < 7:
    print('Game was terminated')