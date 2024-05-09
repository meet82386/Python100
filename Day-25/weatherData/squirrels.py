import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240502.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f"Grey: {gray_squirrels}, Cinnamon: {cinnamon_squirrels}, Black: {black_squirrels}")

data_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

dataframe = pd.DataFrame(data_dict)
# dataframe.to_csv("squirrel_count.csv")