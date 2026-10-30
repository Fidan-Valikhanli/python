tecrube = int(input("Təcrübə illərini daxil edin: "))
bal = int(input("Müsahibə balını daxil edin: "))

if tecrube < 0 or bal < 0 or bal > 100:
    print("Yanlış məlumat")

else:
    result = "Keçdi" if bal >= 90 or (tecrube >= 2 and bal >= 70) else "Keçmədi"

    if bal >= 90:
        print("Güclü namizəd")
    elif tecrube >= 2 and bal >= 70:
        print("Növbəti mərhələyə dəvət olunur")
    else:
        print("Namizəd uyğun deyil")

    print("İlkin seçim:", result)