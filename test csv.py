import csv

with open('unwanted_txt.csv', newline='') as f:
    reader = csv.reader(f)
    csv_data = []
    for row in reader:
        csv_data.append(row)

print(csv_data)
