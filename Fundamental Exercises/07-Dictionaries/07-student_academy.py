n = int(input())
students = {}
for i in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)
students = {key: sum(value)/len(value) for key, value in students.items() if sum(value)/len(value) >= 4.50}
students = dict(sorted(students.items(), key=lambda el: -el[1]))
for key, value in students.items():
    print(f'{key} -> {value:.2f}')
