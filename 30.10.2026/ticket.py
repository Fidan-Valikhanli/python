age = int(input("Enter your age: "))
student = input("Are you a student? (yes?no): ")
if( age < 7):
    print("You get a free ticket")
elif( age > 65):
    print("Ticket price is 4AZN")
elif( student == "yes"):
    print("Ticket price is 5AZN")
else:
    print("Ticket price is  8AZN")