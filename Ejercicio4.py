""" 4.Escribir un script que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña e imprima por 
pantalla si la contraseña introducida por el usuario coincide con la guardada en la 
variable sin tener en cuenta mayúsculas y minúsculas. """

""" Con funcion """
def Contraseña():
    clave = "salathiel";
    contraseña = input("Introduce una contraseña por favor->:");
    if clave == contraseña.lower():
        print("La contraseña coincide");
    else:
        print("La contraseña no coincide");
valor = Contraseña();
input();



""" Sin funcion """

clave = "salathiel";
contraseña = input("Introduce una contraseña por favor->:");
if clave == contraseña.lower():
    print("La contraseña coincide");
else:
    print("La contraseña no coincide");
print("Presiona Enter para salir");
input();
