# # # Control Flow with if / else and Conditional Operators

# print("--------Welcome to the rollercoaster!--------")
# heigth = int(input("What is your heigth in cm? "))
# if heigth >= 120:
#     print("You are tall enough to ride!")
# else:
#     print("You are not tall enough to ride!")
# print("Have a nice day!")
# print("--------Thank you for riding the rollercoaster!--------")

##################
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


##################
# heigth = int(input("What is your heigth in cm? "))
# if heigth >= 120:
#     print("You can ride the rollercoaster! but ???")
#     age = int(input("How old are you? "))
#     if age < 12:
#         print("ticket 5$")
#     elif age <=18:
#         print("ticket 7$")
#     elif age >50:
#         print("omg you will die here. ticket free")
#     else:
#         print("ticket 12$")
# else:
#     print("You are not tall enough to ride!")


##################
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmi = weight / height**2
# rounded_bmi = round(bmi)

# if rounded_bmi < 18.5:
#     print(f"Your BMI is {rounded_bmi}, you are underweight")
# elif rounded_bmi < 25:
#     print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
# elif rounded_bmi < 30:
#     print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
# elif rounded_bmi < 35:
#     print(f"Your BMI is {rounded_bmi}, you are obese.")
# else:
#     print(f"Your BMI is {rounded_bmi}, you are clinically obese.")


##################


# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4

# **except** every year that is evenly divisible by 100

# **unless ** the year is also evenly divisible by 400


# year = int(input("Which year do you want to check? "))
# if year % 4 != 0:
#     print("Not leap year.")
# else:
#     if year % 100 != 0:
#         print("Leap year.")
#     else:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")

# refactoring

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
