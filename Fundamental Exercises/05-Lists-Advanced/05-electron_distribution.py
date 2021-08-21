number_of_electrons = int(input())
electrons = []
shell_number = 1
while number_of_electrons > 0:
    possible_electrons = 2*shell_number**2
    if possible_electrons > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(possible_electrons)

    number_of_electrons -= possible_electrons
    shell_number += 1
print(electrons)
