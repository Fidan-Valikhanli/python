eded = int(input("Eded daxil edin: "))
addim = 0

while eded != 1:
    print(eded)

    if eded % 2 == 0:
        eded = eded // 2
    else:
        eded = eded * 3 + 1

    addim += 1

print(1)
print("Addim sayi:", addim)