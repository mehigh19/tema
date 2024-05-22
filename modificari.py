import json
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

# fc_varstaCsv('output.csv')

def fc_varstaJson(json_file):
    with open(json_file,'r') as jsonFile:
        data=json.load(jsonFile)
        for persoana in data:
            varsta=int(persoana['varsta'])
            persoana['varsta']=varsta+1
    with open(json_file,'w') as jsonFile:
        json.dump(data,jsonFile)

fc_varstaJson('input.json')