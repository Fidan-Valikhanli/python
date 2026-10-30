mebleg = float(input("Sifarişin məbləğini daxil edin: "))

if mebleg < 0:
    print("Yanlış məbləğ")

else:
    if mebleg >= 200:
        yekun = mebleg * 0.80
    elif mebleg >= 100:
        yekun = mebleg * 0.90
    else:
        yekun = mebleg

    result = "Endirim qazandınız" if mebleg >= 100 else "Endirim yoxdur"

    print("Yekun məbləğ:", round(yekun, 2), "AZN")
    print(result)