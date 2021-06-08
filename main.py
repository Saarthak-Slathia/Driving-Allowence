print("Let's Check whether you can drive or not !")

age = int(input("Enter your age: "))
if age < 18:
    print("You cannot drive, as you are too young.")
elif age > 120:
    print("You cannot be a human")
elif age >= 18:
    print("You can drive")
else:
    print("Invalid Input !!! Please try again")