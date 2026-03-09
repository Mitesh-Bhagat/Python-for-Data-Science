import csv

data = [
    ["Name", "Mo. Number", "Email"],
    ["Mitesh", 8200000011, "miteshbhagt@gmail.com"],
    ["Sonu", 8200000012, "sonubhagat@outlook.com"],
    ["Bhagat", 8200000013, "bhagat@gmal.com"],
    ["Ankit", 8200000014,"ankit@gmail.com"],
    ]

with open("data.csv", "w", newline="") as file:
    wr = csv.writer(file)
    wr.writerows(data)

with open("data.csv", "r") as file:
    red = csv.reader(file)
    for row in red:
        print(row)