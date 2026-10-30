bal = int(input("Balınızı daxil edin: "))

if bal < 0 or bal > 100:
    print("Yanlış bal")
elif bal >= 91:
    print("A (Əla)")
elif bal >= 81:
    print("B")
elif bal >= 71:
    print("C")
elif bal >= 61:
    print("D")
elif bal >= 51:
    print("E")
else:
    print("F")