import os
import pandas as pd

# Construct the file path dynamically based on the script's location
# file_path = os.path.join(os.path.dirname(__file__), "weather_data.csv")

# without using pandas, you can read the CSV file like this:
# with open(file_path) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# new approach using pandas:
# data = pd.read_csv(file_path)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

# max_temp = data["temp"].max()
# print(max_temp)

# print(data[(data.temp == data.temp.max())])

# monday = data[(data.day == "Monday")]
# c = monday.temp
# print(c * 9/5 + 32)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv", index=False)

# All above code is for reading and manipulating the weather data from the CSV file.
# The file path is constructed dynamically to ensure that it works regardless of where the script is run from,
# as long as the CSV file is in the same directory as the script.

# Another example of reading a different CSV file,
# in this case, the squirrel census data
file_path = os.path.join(os.path.dirname(__file__), "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = pd.read_csv(file_path)

print(data.columns)
print(data["Primary Fur Color"].unique())
print(data["Primary Fur Color"].value_counts())

# print(len(data[data["Primary Fur Color"] == "Gray"]))
# to_csv_data = data["Primary Fur Color"].value_counts()
# to_csv_data.to_csv("squirrel_count.csv")
