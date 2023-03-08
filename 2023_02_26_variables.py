#introduccion a python 
# variables 
m1="bienvenido al curso python "
m= 10                          #asignamos un valor a la variable m que anteriormente era de tipo string 
n = 25
suma = m+n 
print(suma)
print (m1)

#strings 
frase= 'frases en variables strings'
frase1= "comenzamos utilizando frases"
frase2= 'en variables "strings" '
print(frase1)
print(frase2)

#concatenacion
frase3 = "concatenacion" + " de frases"
print( frase3)
frase_completa = frase1 + ' ' + frase2
print(frase_completa)
print ( frase3 + " para juntar strings")

nombre1= "Cesar"
nombre2= " Artruo"
apellido1= "Mojica"
apellido2= "Ramirez"
nombre_completo= nombre1 + ' ' + nombre2 + ' ' + apellido1 + ' ' + apellido2
print (nombre_completo)

num= "14"
num2= "18"
numeros= num + ' ' + num2
print (numeros)

#metodos
nombre3 = "cesar arturo mojica ramirez".title()
print(nombre3)
minusculas = "Esta Es Una Frase Para Ser Formateada".lower()
print(minusculas)
mayusculas = "Esta Es Una Frase Para Ser Formateada".upper()
print(mayusculas)

#saltos de linea
print("Python")
print("JavaScript")
print("Java")
print("PHP")
print("TypeScript")
print("SQL")
print("COBOL")

print("-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.")
