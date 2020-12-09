import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Find all the rows in data where primary color is gray.
#     data["Primary Fur Color"] == "Gray"
# Then pull those rows out of data into a new (transient) dataframe
#     data[data["Primary Fur Color"] == "Gray"]
# Finally get the length of the new dataframe
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# Create the required dataframe from a dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
dataframe = pandas.DataFrame(data_dict)

# Create the CSV file
dataframe.to_csv("angela.csv")
