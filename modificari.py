import csv

def fc_varstaCsv(csv_file):
    with open(csv_file, 'r', newline='') as csvFile:
        reader = csv.DictReader(csvFile)
        rows = list(reader)    
    for row in rows:
        row['varsta'] = int(row['varsta'])+1  
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

fc_varstaCsv('output.csv')