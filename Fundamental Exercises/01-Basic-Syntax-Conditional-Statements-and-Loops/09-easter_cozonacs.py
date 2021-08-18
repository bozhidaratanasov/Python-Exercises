budget = float(input())
flour_price = float(input())
remaining_budget = budget

colored_eggs = 0
currentCozonacsCount = 0

while remaining_budget > (flour_price + 0.75 * flour_price + ((1.25 * flour_price) / 4)):
    currentCozonacsCount += 1
    remaining_budget -= (flour_price + 0.75 * flour_price + ((1.25 * flour_price) / 4))
    colored_eggs += 3
    if currentCozonacsCount % 3 == 0:
        colored_eggs -= (currentCozonacsCount - 2)
print(f'You made {currentCozonacsCount} cozonacs! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.')