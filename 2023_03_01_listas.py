#listas
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa']
print(colores[3])

print("el color " + colores[0] + " esta en la pisicion 0")
print("el color " + colores[7] + " esta en la pisicion 7")

numeros = ['tres', 'dos', 'cinco', 'cuatro', 'uno']

# posiciones nativas en listas

colores2 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa' , 'blanco', 'naranja']
print("\n\n")
print("el color " + colores2[-1] + " esta en la pisicion 9")
print("el color " + colores2[-7] + " esta en la pisicion 3")
print("el color " + colores2[-5] + " esta en la pisicion 5")
print("el color " + colores2[-2] + " esta en la pisicion 8")
print("el color " + colores2[-10] + " esta en la pisicion 0")

#eliminar 'azul', 'marrón', 'negro' y 'rosa' con comando del (delete)

print("\n\n")
del colores2[-9]
del colores2[3]
del colores2[4]
del colores2[4]
print( colores2)

#eliminar datos de un arreglo con funcion remove

colores2.remove("amarillo")
colores2.remove("rojo")
print("\n\n")
print( colores2)
# eliminar un dato de la lista utilizando la funcion pop

colores3 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

azul = colores3.pop(1)
blanco = colores3.pop(7)
colorG = [azul, blanco]
print("\n\n")
print("El color eliminado y almacenado es:",  azul)
print("El segundo color eliminado y almacenado es:",  blanco)
print( colores3)
print("\n\n")
print(colorG)

#añadir elementos con la funcion append

colores3.append("fuxia")
colores3.append("celeste")
print("\n\n")
print(colores3)

#insertar algun dato en cierta posicion de la lista con la funcion insert

colores3.insert(-5, "magenta")
colores3.insert(-1, "turquesa")
print("\n\n")
print(colores3)

#ordenar una lista alfabeticamente a-z o z-a

print("\n\n")
print("orden alfabetico de la lista de a-z")
colores3.sort()
print(colores3)
print("\n\n")
print("orden alfabetico de la lista de z-a")
colores3.sort(reverse=True)
print(colores3)
print(sorted(colores3))

# contar los elementos de una lista 
print("\nnumero de elementos de la lista colores es de:", len(colores3))

# tuplas
colorestupla = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja') #tupla
print("\n" + colorestupla[1])

numerostupla = (10, 1, 5, 11) 
resultado = numerostupla[0] + numerostupla[2] + numerostupla[3] - numerostupla[1]
print("\n")
print(resultado)

#convercion de lista a tupla y de tupla lista

tuplacolor= tuple(colores3)
print("\n")
print(type(tuplacolor))

listacolor= list(tuplacolor)
print("\n")
print(type(listacolor))