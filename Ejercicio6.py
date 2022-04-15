""" 6.Escribir un script que pida al usuario un número entero 
y muestre por pantalla si es par o impar. """

""" Con funcion """
def numeros_impar_o_par():
    number = int(input("Ingresa un numero entero por favor:D ->"))
    if number % 2 == 0:
        print("Este numero es: ", str(number), "Es par");
    else:
        print("Este numero es: ", str(number), "Es impar");
valor = numeros_impar_o_par()
print("Presiona enter para salir del script")
input()

""" number % 2 == 0es una expresión booleana válida que comprueba si number % 2es equivalente a 0. Para numbers pares, 
el resultado es el valor, True. """

""" Sin funcion """
number = int(input("Ingresa un numero entero por favor:D ->"))
if number % 2 == 0:
    print("Este numero es: ", str(number), "Es par");
else:
    print("Este numero es: ", str(number), "Es impar");
print("Presiona enter para salir del script");
input();