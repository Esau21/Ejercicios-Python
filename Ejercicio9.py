""" 9.Escribir un script que pregunte el nombre completo del usuario en la 
consola y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo 
con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su 
nombre combinando mayúsculas y minúsculas como quiera. """

""" Con funcion """
def Nombre_Completo():
    print("Escribe tu nombre")
    nombre = input("Ingresa tu nombre por favor :D ->")
    print(nombre.lower());
    print(nombre.upper());
    print(nombre.title());
valor = Nombre_Completo();
print("Presiona enter para salir")
input()

""" Sin funcion """
print("Escribe tu nombre")
nombre = input("Ingresa tu nombre por favor :D ->")
print(nombre.lower());
print(nombre.upper());
print(nombre.title());
print("Presiona enter para salir")
input()

