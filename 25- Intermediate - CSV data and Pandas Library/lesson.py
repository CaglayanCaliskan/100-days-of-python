# with open('./weather_data.csv') as data_file:
#     data = data_file.read().split()
#     print(data[1])


# import csv

# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)


import pandas

data = pandas.read_csv('./weather_data.csv')
# # print(type(data))
# # temp = data["temp"]
# # print((temp))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(sum(temp_list) / len(temp_list))

# print(data['temp'].max())

# # Get Data in columns

# print(data["condition"])
# print("s2", data.condition)

# Get Data in Row

# print(data[data.day == "Monday"])


# Get Max temp from colomn
# print(data[data.temp == data.temp.max()])

# def convert_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32


# monday_temp = data[data.day == 'Monday'].temp
# print(convert_to_fahrenheit(int(monday_temp)))


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
