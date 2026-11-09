num = int(input("Eded daxil edin: "))

factorial = 1

if num < 0:
    print("Menfi ededin faktoriali yoxdur")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Faktorial:", factorial)