product = input()
resources = {}
while not product == 'stop':
    quantity = int(input())
    if product not in resources:
        resources[product] = 0
    resources[product] += quantity
    product = input()

for key, value in resources.items():
    print(f'{key} -> {value}')
