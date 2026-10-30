n = int(input("Enter digit: "))
a = n //1000
b = (n // 100) % 10
c = (n// 10) % 10
d = n % 10
sum = a + b + c + d
print(f"The sum of the digits is: {sum}")