#declarar funciones 

def suma(numero1, numero2):
	print(numero1 + numero2)

suma(10, 20)
suma(20, 30)
suma(50000, 7000)

#identificar numero de arumentos que tiene la funcion 

print("\n")
def colores(*args):
	print(len(args))

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#utilizacion de argumentos de la funcion   

print("\n")
def colores2(*args):
	print("El color", args[1], "es mi favorito.", "\nEl color", args[0], "tampoco está mal.")

colores2('rojo', 'azul')

#utilizacion de arumentos para realizar operaciones 

print("\n")
def operacion(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print("El resultado es:", resultado)

operacion(12, 5, 9, 17, 6, 14)

#argumentos arbitrarios

def colores1(**kwargs):
	print("Este es el color " + kwargs['color1'] )

colores1(color1='rojo', color2='azul')
