price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))
amount = price * (discount / 100)
sale = price - amount
print(f"The amount of discount is: {amount:.2f}")
print(f"The sale price of the item is: {sale:.2f}")