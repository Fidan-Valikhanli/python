qiymet = float(input("İlkin qiymet: "))
endirim = float(input("Endirim faizi: "))

mebleg = qiymet * endirim / 100
son = qiymet - mebleg

print("Endirim meblegi:", mebleg)
print("Son qiymet:", son)