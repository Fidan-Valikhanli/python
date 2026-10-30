mebleg = float(input("Sifaris meblegini daxil edin(AZN): "))
if mebleg < 0:
    print("Xeta: Mebleg menfi ola bilmez.")
elif mebleg < 100:
    print("Endirim yoxdur. Yekun mebleg: {mebleg:.2f} AZN")
else:
    endirim_faizi = 20 if mebleg >= 200 else (10 if mebleg >= 100 and mebleg < 200)
    endirim_meblegi = mebleg*endirim_faizi /100
    yekun_mebleg = endirim_meblegi - mebleg
print(f"Yekun mebleg: {yekun_mebleg:.2f} AZN")





