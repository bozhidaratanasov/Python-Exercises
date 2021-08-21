courses = {}
string = input()
while not string == 'end':
    course, student = string.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    string = input()

courses = dict(sorted(courses.items(), key=lambda el: -len(el[1])))
for value in courses.values():
    value.sort()
for key, value in courses.items():
    print(f'{key}: {len(value)} ')
    for el in value:
        print(f'-- {el}')
