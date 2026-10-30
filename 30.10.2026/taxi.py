mesafe = float(input("Məsafəni daxil edin (km): "))
saat = int(input("Saatı daxil edin (0-23): "))

if mesafe < 0 or saat < 0 or saat > 23:
    print("Yanlış məlumat")
else:
    qiymet = 2 + mesafe * 0.80

    if qiymet < 3:
        qiymet = 3

    if saat >= 23 or saat < 6:
        qiymet = qiymet * 1.20

    print("Gediş haqqı:", round(qiymet, 2), "AZN")