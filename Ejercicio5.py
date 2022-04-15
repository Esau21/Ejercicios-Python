""" 5.Escribir un script que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el script debe mostrar un error. """

""" Con funcion """
def dividir(a, b):
    print("Divison de numeros")
    a = float(input("Introduce el numero dividendo Por favor->"))
    b = float(input("Introduce el numero a dividir Por favor->"))
    if b == 0:
        print("¡Failed! Estos numeros no se pueden dividir por 0.")
    else:
        print("Felicidades estos dos numeros si se pueden divir la respuesta es->")
        print(a/b)
valor = dividir(a='', b='');
print("Presiona la tecla enter para salir :D")
input()


""" Sin funcion """
print("Divison de numeros")
a = float(input("Introduce el numero dividendo Por favor->"))
b = float(input("Introduce el numero a dividir Por favor->"))
if b == 0:
    print("¡Failed! Estos numeros no se pueden dividir por 0.")
else:
    print("Felicidades estos dos numeros si se pueden divir la respuesta es->")
    print(a/b)
print("Presiona la tecla enter para salir :D")
input()
