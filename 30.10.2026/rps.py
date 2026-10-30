oyuncu1 = input("1-ci oyunçu: ")
oyuncu2 = input("2-ci oyunçu: ")

if (oyuncu1 != "daş" and oyuncu1 != "qayçı" and oyuncu1 != "kağız") or (oyuncu2 != "daş" and oyuncu2 != "qayçı" and oyuncu2 != "kağız"):
    print("Belə seçim yoxdur")

elif oyuncu1 == oyuncu2:
    print("Heç-heçə")

elif oyuncu1 == "daş" and oyuncu2 == "qayçı":
    print("1-ci oyunçu qalibdir")

elif oyuncu1 == "qayçı" and oyuncu2 == "kağız":
    print("1-ci oyunçu qalibdir")

elif oyuncu1 == "kağız" and oyuncu2 == "daş":
    print("1-ci oyunçu qalibdir")

else:
    print("2-ci oyunçu qalibdir")