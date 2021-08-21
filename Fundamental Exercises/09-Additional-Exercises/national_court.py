first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
total_clients_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
people_count = int(input())
for i in range(1, people_count):
    if i % 4 == 0:
        continue
    people_count -= total_clients_per_hour
    if people_count <= 0:
        print(f'Time needed: {i}h.')
        break
