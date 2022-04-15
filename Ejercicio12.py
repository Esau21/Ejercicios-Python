""" 12.	Escribir un script que pregunte el nombre del usuario en la consola y después de que el 
usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> 
es el nombre que el usuario haya introducido. """

def name():
    print("Escribi tu nombre en la consola");
    nombre = input("Introduce tu nombre :D ->");
    for i in range(10):
        print("¡Hola " , nombre , "!");
value = name();
print("Por favor presiona para salir :D");
input();

print("Escribi tu nombre en la consola");
nombre = input("Introduce tu nombre :D ->");
for i in range(10):
    print("¡Hola " , nombre , "!");

print("Por favor presiona para salir :D");
input();
