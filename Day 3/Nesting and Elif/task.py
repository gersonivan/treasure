print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 6%")
    elif age <= 18:
        print("Please pay %7 ")
    elif age < 22:
        print("Please pay $8")
    else:
        print("Please pay $12 ")
else:
    print("Sorry you have to grow taller before you can ride.")
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi <18.5:
    print("underweight")
elif bmi <25:
    print ("normal")
else:
    print("overweight")
