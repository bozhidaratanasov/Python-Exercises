items = input().split('|')
budget = float(input())
new_item_prices = []
profit = 0
total_spent = 0
total_earned = 0
end_budget = 0
for string in items:
    item_type, value = string.split('->')
    value = float(value)
    if item_type == 'Accessories' and value > 20.50:
        continue
    elif item_type == 'Shoes' and value > 35.00:
        continue
    elif items == 'Clothes' and value > 50.00:
        continue
    if budget >= value:
        budget -= value
    elif budget < value:
        break
    new_value = value * 1.4
    new_item_prices.append(new_value)
    total_spent += value
    total_earned += new_value
    profit = total_earned - total_spent
end_budget = budget + sum(new_item_prices)
for element in new_item_prices:
    print(f'{element:.2f} ', end='')
print('')
print(f'Profit: {profit:.2f}')
if end_budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
