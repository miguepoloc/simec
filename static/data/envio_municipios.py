import os
import requests

url = 'http://127.0.0.1:8010/api/Municipio/'

print('>> LECTURA DATOS MUNICIPIOS <<')

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
f = open("Municipios.csv", "r", encoding="utf8")
for x in f:
    y = x.split("\n")
    codigo_departamento, departamento, codigo_municipio, municipio, tipo_municipio = y[0].split(
        ";")

    if (tipo_municipio == "Municipio"):
        tipo = 1
    elif (tipo_municipio == "Isla"):
        tipo = 3
    else:
        tipo = 2

    myobj = {"codigo_municipio": codigo_municipio, "nombre_municipio": municipio,
             'departamento': codigo_departamento, 'tipo_municipio': tipo}
    # print(myobj)
    x = requests.post(url, data=myobj)

f.close()
