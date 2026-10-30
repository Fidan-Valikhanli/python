gelir = float(input("Aylıq gəliri daxil edin: "))
xerc = float(input("Ümumi xərcləri daxil edin: "))

if gelir < 0 or xerc < 0:
    print("Yanlış məbləğ")

else:
    qalan = gelir - xerc

    print("Qalan pul:", round(qalan, 2), "AZN")

    if gelir == 0:
        faiz = 0
        print("Qənaət faizi hesablana bilməz")

    else:
        faiz = (qalan / gelir) * 100
        print("Qənaət faizi:", round(faiz, 2), "%")

    if xerc > gelir:
        print("Büdcə kəsiri var")
    elif gelir == 0:
        print("Büdcə normaldır")
    elif xerc >= gelir * 0.80:
        print("Xərclərə diqqət et")
    elif xerc >= gelir * 0.50:
        print("Büdcə normaldır")
    else:
        print("Yaxşı qənaət edirsiniz")