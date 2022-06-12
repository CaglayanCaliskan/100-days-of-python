# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
total_len = 0
for height in student_heights:
    total_height += height
    total_len += 1
average_height = round(total_height / total_len)
print(f"{average_height}")


# Write your code below this row 👇
# 180 124 165 173 189 169 146
