#################
heigth = int(input("What is your heigth in cm? "))
bill = 0
if heigth >= 120:
    print("You can ride the rollercoaster! but ???")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    elif age >= 45 and age <= 55:
        print("omg you will die here. Aduly tickets are free")
    else:
        bill = 12
        print("ticket 12$")

    wants_photo = input("Do you wanna photo taken ? Y or N ")
    if wants_photo == "Y":
        # Add $3 their bill
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("You are not tall enough to ride!")
