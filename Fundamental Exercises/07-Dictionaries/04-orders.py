product_quantity = {}
product_price = {}
string = input()
while not string == 'buy':
    product, price, quantity = string.split()
    price = float(price)
    quantity = int(quantity)
    if product not in product_quantity:
        product_quantity[product] = quantity
        product_price[product] = price
    else:
        product_quantity[product] += quantity
        product_price[product] = price
    string = input()

result = {el: product_quantity[el]*product_price[el] for el in product_quantity}
for key, value in result.items():
    print(f'{key} -> {value:.2f}')
