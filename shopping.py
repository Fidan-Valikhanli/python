price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
spent = price*quantity
money = float(input("Enter the money you have: "))
remaining = money - spent
print(f"Remaining money:{remaining:.2f}")

