print("Hola Mundo con Python")

#enviar un saludo a la consola utilizando python
print("Este es mi saludo desde Python...")

#uso de una variable
miVariable = "Hola desde Python"
print( miVariable )

#cambio del valor de la variable
miVariable = 10
print( miVariable )

#operar con variables
x = 1
y = 2
z = x + y
print(z)

#direcciones de memoria
print(id(x))

#uso de variables
nombre = "Diego Katz"
telefono = 3424186471
email = "diekatz@gmail.com"
adulto = True
peso = 95.7

print(nombre)
print(telefono)
print(email)

#tipo de datos
print(type(nombre))
print(type(telefono))
print(type(adulto))
print(type(peso))

#Concatenacion
miGrupoFavorito = "Bob Marley"
print("Mi grupo favorito es: " + miGrupoFavorito)
print("Mi grupo favorito es:", miGrupoFavorito)

#Conversion de tipo de dato
numero1="1"
numero2="2"
print("Concatenacion:",numero1+numero2)
print("Suma:", int(numero1) + int(numero2))

#tipos Boolean (bool)
miVariable = True
print(miVariable)

miVariable = 3<2
print(miVariable)

if miVariable:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Funcion input (siempre regresa un string)
resultado = input("Escribe el mensaje:")
print("Mensaje:", resultado)

#Ejercicio detalle del libro
titulo = input("Proporciona el titulo del libro: ")
autor = input("Proporciona el autor del libro: ")
print("Titulo del libro es: ", titulo)
print("El autor del libro es:", autor)
print(titulo, "fue escrito por", autor)

operandoA = 3
operandoB = 2
suma = (operandoA + operandoB)
#print('El resultado de la suma es:', suma)
print(f'El resultado de la suma es: {suma} ')
resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta} ')
multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion} ')
division = operandoA / operandoB
print(f'El resultado de la division es: {division} ')
division = operandoA // operandoB
print(f'El resultado de la division es (int): {division} ')
modulo = operandoA % operandoB
print(f'El residuo de la division es: {modulo} ')
exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente} ')

#Ejercicio rectangulo
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Propoprciona el ancho del rectangulo: '))
print(f'El alto del rectangulo es: {alto}')
print(f'El ancho del rectangulo es: {ancho}')
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')
#final
