""" 2.	Escribir un script que solicite el nombre, 
edad y apellido de un usuario y muéstrelo por pantalla """

""" Con funcion """
def datos(nombre, edad, apellido):
    print("Ingresa los siguientes datos")
    print("Ingresa tu nombre")
    nombre = input()
    print("Ingresa tu edad")
    edad = input()
    print("Ingresa tu apellido")
    apellido = input()
    print("Tu nombre es: ", nombre)
    print("Tu edad es: ", edad)
    print("Tu apellido es: ", apellido)
    resultado = nombre + edad + apellido;
    return resultado;
valor = datos(nombre='', edad='', apellido='')
print("Presiona Enter para poder salir")
input()

print("Ingresa los siguientes datos")
print("Ingresa tu nombre")
nombre = input()
print("Ingresa tu edad")
edad = input()
print("Ingresa tu apellido")
apellido = input()
print("Tu nombre es: ", nombre)
print("Tu edad es: ", edad)
print("Tu apellido es: ", apellido)
print("Presiona Enter para poder salir")
input()