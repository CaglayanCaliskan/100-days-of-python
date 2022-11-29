import pandas
import random
number = [1, 2, 3]
new_list = []
for n in number:
    add_1 = n + 1
    new_list.append(add_1)

print("new_list: ", new_list)

# List Comprehension
newest_list = [n+1 for n in number]
print("newest_list:", newest_list)


name = "Caglayan"
name_list = [n for n in name]
print(name_list)


doubled = [n*2 for n in range(1, 5)]
print(doubled)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

small = [n.upper() for n in names if len(n) > 4]
print(small)

# Dict Comprehension
students_score = {student: random.randint(1, 100) for student in names}
print("students_score:", students_score)

passed_students = {student: score for (
    student, score) in students_score.items() if score >= 60}
print("passed_students:", passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for (word) in sentence.split()}

print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def convert_to_f(c):
    return (c * 9/5) + 32


weather_f = {key: convert_to_f(int(value))
             for (key, value) in weather_c.items()}

print("weather_f", weather_f)


# Looping through dictinaries:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

# Loop through a date frame

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a date frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
