correct_email:"user@gmail.com"
correct_password:"user123"
email = input("Enter your email: ")
password = input("Enter your password: ")
if (email != correct_email ):
    print("Account not found.")
elif(password != correct_password):
    print("Incorrect password.")
else:
    print("Welcome!")
    