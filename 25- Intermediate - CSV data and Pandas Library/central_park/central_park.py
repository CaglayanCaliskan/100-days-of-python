import pandas
data = pandas.read_csv(
    './2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray = (len(data[data["Primary Fur Color"] == 'Gray']))
red = (len(data[data["Primary Fur Color"] == 'Cinnamon']))
black = (len(data[data["Primary Fur Color"] == 'Black']))

print(gray)
print(red)
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Colors_file.csv")
