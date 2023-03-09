# condicional if 

num1 = 15
num2 = 20

if num1 < num2:
	print("Se ejecuta el if.")
 
num3 = 1450
num4 = 60

if num3 > num4:
	print("Se ejecuta el if.")
 
num5 = 60
num6 = 60

if num1 != num2:
	print("Se ejecuta el if.")
 
# condicional if, else

color = "rojo"

if color != "rojo":
    print("\n El color no es rojo.")
else:
    print ("\n El color es rojo.")

# condicional if, elif, else

edad = int(input("¿Cuál es tu edad?\n"))
if edad <= 0:
	print("Nadie puede tener esa edad.")
elif edad >= 1 and edad <= 18:
	print("Eres menor de edad.")
elif edad > 18 and edad <= 45:
	print("Eres mayor de edad.")
elif edad > 45 and edad <= 100:
	print("Eres una persona grande")
elif edad > 100 and edad <= 120:
	print("Eres muy grande")
else:
	print("Edad no válida.")
 
 #condicionales en listas
 
color = input("Introduce un color:\n")
tuplacolor = ('cafe', 'gris', 'rojo', 'verde','naranja', 'negro', 'blanco', 'rosa')
print ("\n")
if color in tuplacolor[0]:
	print("El color cafe está admitido")
elif color in tuplacolor[1]:
	print("El color gris está admitido")
elif color in tuplacolor[2]:
	print("El color rojo está admitido")
elif color in tuplacolor[3]:
	print("El color verde está admitido")
elif color in tuplacolor[4]:
	print("El color naranja está admitido")
elif color in tuplacolor[5]:
	print("El color negro está admitido")
elif color in tuplacolor[6]:
	print("El color blanco está admitido")
elif color in tuplacolor[7]:
	print("El color rosa está admitido")
else:
	print('color no admitido')
 
# multiples if
 
entrada = int(input('Introduce un número del 1 al 4:\n'))

if entrada == 1:
    print('Has seleccionado la opción número 1.')
if entrada == 2:
    print('Has seleccionado la opción número 2.')
if entrada == 3:
    print('Has seleccionado la opción número 3.')
if entrada == 4:
    print('Has seleccionado la opción número 4.')

# if, and, or 

if num1 < num2 :
    print ("\n El numero 1 es menor que el numero 2")
if num1 < num2 and num1 < num3:
    print ("\n El numero 1 es menor que el numero 2 y el numero 3")
if num1 < num2 or num1 < num3:
    print ("\n El numero 1 es menor que alguno de los otros 2 numeros")
 