import csv
data = [
    ["Name", "Salary"],
    ["Mitesh ->", 50000],
    ["Bhagat ->", 40000],
    ["Sonu ->", 60000]
]

#wirte
with open ("Salary.csv","w",newline="") as file:
    wri = csv.writer(file)
    wri.writerows(data)

#read
with open ("Salary.csv","r") as file:
    red = csv.reader(file)
    for row in red:
        print(row)