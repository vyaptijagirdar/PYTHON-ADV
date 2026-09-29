import csv
import json

input_file = "students.csv"
output_file = "students.json"

with open(input_file, "r") as file:
    data = list(csv.DictReader(file))

with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print("Conversion successful")
