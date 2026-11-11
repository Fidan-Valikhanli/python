number = int(input("Axtarilan reqemi daxil edin (1-100): "))
count = 0
user_number = int(input("1-100 arasinda eded daxil edin: "))
while user_number != number:
    count = count +1

    if user_number < number:
        print("Daha boyuk eded yazin")
    else:
        print("Daha kicik eded yazin")

    user_number = int(input("Yeniden eded daxil edin: "))

count = count +1

print("Duzgun ededi tapdiniz.")
print("Cehd sayi: ", count)
