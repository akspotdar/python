import os
# List Comprehension Examples:

numbers = [1, 2, 3, 4, 5]
plus_one = [num + 1 for num in numbers]
print(plus_one)

# Squared Numbers:
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Filtered List Comprehension:
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Nested List Comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

letters_list = [ letter for letter in "Hello World" if letter != " "]
print(letters_list)

double_range = [num*2 for num in range(1,5)]
print(double_range)

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Example of reading two files and finding common numbers using list comprehension
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("file1.txt", "r")
file1 = f.readlines()
file1 = [int(line.strip()) for line in file1]
print(file1)

f = open("file2.txt", "r")
file2 = f.readlines()
file2 = [int(line.strip()) for line in file2]
print(file2)

result = [num for num in file1 if num in file2]
print(result)

# Dictionary Comprehension Examples:

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
name_length = {name: len(name) for name in names}
print(name_length)

name_dict = {key: value for (key, value) in name_length.items() if value > 3}
print(name_dict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# result = {word: len(word) for word in words}
result = {word: len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = { day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items() }
print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# print('Angela' in student_dict["student"])
# print(student_dict["score"][student_dict["student"].index("Angela")])
for (key, value) in student_dict.items():
    print(f'{key}: {value}')

# student_score = { student: score for (student, score) in zip(student_dict["student"], student_dict["score"]) }
# print(student_score)

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through rows of a dataframe
for (index, row) in student_df.iterrows():
    print(row)
    # print(row.student)
    # print(row.score)

