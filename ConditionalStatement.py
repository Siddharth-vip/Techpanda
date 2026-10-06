# Amusement Park Ride Eligibility

age = int(input("Enter your age: "))
height = int(input("Enter your height (in cm): "))

if age >= 18 and height >= 150:
    print("You can enjoy all rides.")

elif (age >= 15 and height >= 140) or height >= 170:
    print("You can enjoy most rides.")

elif age >= 12 or height >= 130:
    print("You can enjoy children's rides.")

else:
    print("You are not eligible for the rides.")