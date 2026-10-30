n = int(input("Enter digit: "))
if (n % 3 == 0):
    print("Fizz")
    if (n%5 == 0):
        print("Buzz")
    elif (n%3 == 0 and n%5 == 0):
        print("FizzBuzz")
        