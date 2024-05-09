# CSV => Comma Separated Values
import csv
import pandas as pd

data = pd.read_csv("weather_data.csv")
temperature = data.temp
# temperature = data["temp"]


print(f"Average Temperature is: {temperature.mean()}")
print(f"Maximum Temperature is: {temperature.max()}")

# Get data in row

# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()].condition)
