import os
import requests

url = 'http://127.0.0.1:8010/api/Centro_Poblado/'

print('>> LECTURA DATOS CENTROS POBLADOS <<')

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
f = open("Centros_Poblados.csv", "r", encoding="utf8")
for x in f:
    y = x.split("\n")
    codigo_departamento, departamento, codigo_municipio, municipio, codigo_centro_poblado, centro_poblado, tipo_centro_poblado = y[0].split(
        ";")

    if (tipo_centro_poblado == "CM"):
        tipo = 1
    elif (tipo_centro_poblado == "CP"):
        tipo = 2
    else:
        tipo = 3

    myobj = {"codigo_centro_poblado": codigo_centro_poblado, "nombre_centro_poblado": centro_poblado,
             'municipio': codigo_municipio, 'departamento': codigo_departamento, 'tipo_centro_poblado': tipo}
    # print(myobj)
    x = requests.post(url, data=myobj)

f.close()
