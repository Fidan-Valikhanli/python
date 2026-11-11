a = 0
b = 1
say = 0

while a < 1000:
    print(a)
    
    c = a + b
    a = b
    b = c

    say += 1

print("Ededlerin sayi:", say)