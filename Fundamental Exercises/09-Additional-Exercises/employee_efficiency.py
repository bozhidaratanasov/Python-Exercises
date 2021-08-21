first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
total_clients_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
people_count = int(input())
time = 0
while people_count > 0:
    time += 1
    people_count -= total_clients_per_hour
    if time % 4 == 0:
        time += 1

print(f'Time needed: {time}h.')
