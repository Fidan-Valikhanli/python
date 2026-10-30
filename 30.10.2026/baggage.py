ceki = float(input("Çamadanın çəkisini daxil edin: "))
bilet = input("Bilet növünü daxil edin (econom/business): ")

if ceki < 0:
    print("Yanlış çəki")
elif ceki > 32:
    print("Çamadan qəbul edilmir")
elif bilet == "econom":
    if ceki <= 23:
        print("Pulsuz")
    else:
        print("30 AZN əlavə ödəniş")
elif bilet == "business":
    print("Pulsuz")
else:
    print("Yanlış bilet növü")