import pandas as pd


def save_to_csv(cafe, location, open, close, coffee, wifi, power):
    df = pd.read_csv('cafe-data.csv')

    new_row = {"Cafe Name": cafe, "Location": location, "Open": open,
               close: "6PM", "Coffee": coffee, "Wifi": wifi, "Power": power}

    df = df.append(new_row, ignore_index=True)

    # Save the updated DataFrame to the CSV file
    df.to_csv("cafe-data.csv", index=False)
