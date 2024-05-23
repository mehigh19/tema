import json
import csv

def fc_persoane():
    lista=[]
    while True:
        check=input('introdu nume,prenume, varsta.Daca vrei sa iesi scrie done: ')
        if check!='done':
            nume=input('Introdu nume: ')
            prenume=input('Introdu prenume: ')
            varsta=input('Introdu varsta: ')
            dict={
                'nume':nume,
                'prenume':prenume,
                'varsta':varsta,
            }
            lista.append(dict)
        else:
            return lista
        
def fc_json():
    with open('input.json','w') as file:
        json.dump(fc_persoane(),file)

# fc_json()

def JsonToCsv(input_file,output_file):
    with open(input_file,'r') as json_file:
        data=json.load(json_file)
        headers = data[0].keys()
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

JsonToCsv('input.json','output.csv')