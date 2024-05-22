import json

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

fc_json()