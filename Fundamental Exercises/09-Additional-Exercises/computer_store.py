total_price_without_taxes = 0
total_taxes = 0
price = input()
while not price == 'regular' and not price == 'special':
    price = float(price)
    if price < 0:
        print('Invalid price!')
        price =input()
        continue
    total_price_without_taxes += price
    total_taxes += 0.2 * price
    price = input()

total_price = total_price_without_taxes + total_taxes
if total_price == 0:
    print('Invalid order!')
elif price == 'regular':
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes:{total_price_without_taxes: .2f}$\n"
          f"Taxes:{total_taxes: .2f}$\n-----------\nTotal price:{total_price: .2f}$")
elif price == 'special':
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes:{total_price_without_taxes: .2f}$\n"
          f"Taxes:{total_taxes: .2f}$\n-----------\nTotal price:{total_price - 0.1*total_price: .2f}$")
