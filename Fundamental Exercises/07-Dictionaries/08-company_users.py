string = input()
companies = {}
while not string == 'End':
    company_name, employee_id = string.split(' -> ')
    if company_name not in companies:
        companies[company_name] = []
    if employee_id in companies[company_name]:
        string = input()
        continue
    companies[company_name].append(employee_id)
    string = input()

companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for key, value in companies.items():
    print(key)
    for el in value:
        print(f'-- {el}')
