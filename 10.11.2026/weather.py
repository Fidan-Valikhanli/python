temperatures = [-3, 2, 8, 15, 22, 27, 31]

day = 1

for temp in temperatures:
    if temp < 0:
        weather = "Şaxta"
    elif temp <= 9:
        weather = "Soyuq"
    elif temp <= 19:
        weather = "Mülayim"
    elif temp <= 29:
        weather = "İsti"
    else:
        weather = "Çox isti"

    print(day, "-ci gün:", str(temp) + "°", "->", weather)
    day = day + 1