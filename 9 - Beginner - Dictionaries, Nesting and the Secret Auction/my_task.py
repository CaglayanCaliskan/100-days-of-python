from os import system
dic = {"name": "caglayan", "lastname": "caliskan"}
dic["city"] = "izmir"
print(dic["city"])

capitals = {
    "Germany": "Berlin",
    "Turkey": "Ankara"
}


travel_log = {
    "Germany": {
        "cities_visited": ["Hamburg", "Bremen", "Munich"]
    },
    "Turkey": ["Izmir", "Istanbul", "Antalya"]
}


print(travel_log["Germany"]["cities_visited"])
system('cls')
