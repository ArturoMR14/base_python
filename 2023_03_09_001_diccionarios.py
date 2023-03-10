#diccionario

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print("El modelo", teclado2["Modelo"], "cuesta", teclado2["Precio"], "$")

#recorrido de un diciionario

for x in teclado1:
	print(x, "=", teclado1[x] + ".")
 
print("\n")
 
for x2 in teclado2:
    print(x2)
    print(teclado2[x2])
    
    
#saber el numero tottal de datos guardados

print("\n")
print(len(teclado1))
print(len(teclado2))

#borrar datos de un diciionario 

print("\n")
del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])

#añadir datos a un diciionario 

print("\n")
teclado2['Color'] = 'Negro'
print(teclado2)
print(len(teclado2))