import csv

with open("People.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)