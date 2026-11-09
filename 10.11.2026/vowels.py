word = input("Soz ve ya cumle daxil edin: ")

vowels = "aeeıioöuüəAEIİOÖUÜƏ"
count = 0

for letter in word:
    if letter in vowels:
        count = count + 1

print("Saitlerin sayi:", count)