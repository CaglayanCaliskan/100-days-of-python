# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

names = name1 + name2

t = names.lower().count("t")
r = names.lower().count("r")
u = names.lower().count("u")
e = names.lower().count("e")
true_total = t+r+u+e
l = names.lower().count("l")
o = names.lower().count("o")
v = names.lower().count("v")
e = names.lower().count("e")
love_total = l+o+v+e

result = int(str(true_total) + str(love_total))

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result < 50 and result > 40:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
