import os
import requests

url = 'http://127.0.0.1:8010/api/Departamento/'

print('>> LECTURA DATOS DEPARTAMENTOS <<')

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
f = open("Departamentos.csv", "r", encoding="utf8")
for x in f:
    y = x.split("\n")
    codigo, departamento = y[0].split(";")
    myobj = {'codigo_departamento': codigo,
             'nombre_departamento': departamento}
    print(myobj)
    x = requests.post(url, data=myobj)

f.close()
