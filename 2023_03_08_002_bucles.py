# bucle while 

x =0
while x <= 15:
    print("X vale:")
    print(x)
    x += 5
 
x2 =0
while x2 >= -100:
    print("X vale:")
    print(x2)
    x2 -= 20

x3= 10
while x3 >= 0:
    print("X vale:")
    print(x3)
    x3 -= 1
    
#while con if 

x4 = 0
while x4 <= 30:
	x4 += 1 
	if x4 == 4 or x4 == 6 or x4 == 10:
		print("Se saltó el valor ", x4, "de x")
		continue

	if x4 == 15:
		print("Se rompió la ejecución del bucle cuando x valía:" , x4)
		break
    
	print("el valor del bucle es: ", x4)
 
#bucle for 

colores = ('rojo', 'azul', 'verde', 'amarillo')

for x5 in colores:
	print("El color es:  "+ x5 )
 
print("\n")
for x6 in colores:
    print("EL COLOR ES:  "+ x6 )
    if x6 == "azul":
        pass
        print("El color que nos brincamos es:  "+ x6 )

print("\n")
for x7 in colores:
    print("el color es:  "+ x7 )
    if x7 == "azul":
        break

# bucle for in range

for x8 in range(7, 700, 100):
	print(x8)
