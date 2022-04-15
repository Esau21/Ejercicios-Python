""" 3.	Escribir un script que pregunte al usuario su edad y muestre por pantalla
 si es mayor de edad o no. (mayor de edad deber ser mayor de 18 años) """

""" Con funcion """
def mayor_de_edad_o_no():
    print("Ingresa los siguientes datos de tu edad");
    edad = int(input("¿Dime cual es tu edad?->"));
    if edad < 18:
        print("Eres menor de edad");
    else:
        print("Eres mayor de edad");
valor = mayor_de_edad_o_no()
print("Presiona la tecla enter para salir")
input()


""" Sin funcion """

print("Ingresa los siguientes datos de tu edad");
edad = int(input("¿Dime cual es tu edad?->"));
if edad < 18:
    print("Eres menor de edad");
else:
    print("Eres mayor de edad");
print("Presiona la tecla enter para salir")
input()

