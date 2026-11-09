password = input("Şifrəni daxil edin: ")

upper = 0
lower = 0
digit = 0
other = 0

for char in password:
    if char.isupper():
        upper = upper + 1
    elif char.islower():
        lower = lower + 1
    elif char.isdigit():
        digit = digit + 1
    else:
        other = other + 1

print("Böyük hərf:", upper)
print("Kiçik hərf:", lower)
print("Rəqəm:", digit)
print("Digər simvol:", other)

if len(password) > 8 and upper > 0 and lower > 0 and digit > 0 and other > 0:
    print("Şifrə güclüdür")
else:
    print("Şifrə zəifdir")