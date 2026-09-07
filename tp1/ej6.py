dict = {
    'Tomas': 7,
    "Gonzalo": 9,
    "Francisco": 10
}
#primera forma
suma = 0
for key in dict:
    suma = suma + dict[key]

prom = suma / len(dict)
print(f"El promedio es {prom}")

#segunda forma
print(f"El promedio es {sum(dict.values()) / len(dict)}")
    #usamos dict.values() que nos da una lista de los valores del diccionario
    #usamos len() que nos da la longitud del objeto pasado como parametro.