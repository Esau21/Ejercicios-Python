""" 7.Escribir un script para una empresa que tiene salas de juegos para todas las edades
 y quiere calcular de forma automática el precio que debe cobrar a sus clientes 
 por entrar. El script debe preguntar al usuario la edad del cliente y mostrar
el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene
 entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10 """

""" Con funcion """
def Empresa():
    print("BIENVENIDOS A LA EMPRESA DE JUEGOS TOYS")
    Edad = int(input("Ingresa tu edad por favor :D ->"))
    if Edad < 4:
        price = 0
    elif Edad <= 18:
        price = 5
    else:
        price = 10
    print("El precio de la entrada es: ", price, "$.");
valor = Empresa()
print("Presiona enter para salir del script :D");
input();

""" Sin funcion """
print("BIENVENIDOS A LA EMPRESA DE JUEGOS TOYS")
Edad = int(input("Ingresa tu edad por favor :D ->"))
if Edad < 4:
    price = 0
elif Edad <= 18:
    price = 5
else:
    price = 10
    print("El precio de la entrada es: ", price, "$.");