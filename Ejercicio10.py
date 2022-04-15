""" 10.	Escribir un script que pregunte el nombre del usuario 
en la consola y después de que el usuario lo introduzca muestre por pantalla
 <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de 
 letras que tienen el nombre. """

""" Con funcion """
def nombre_usuario_consola():
    print("Ingresa tu nombre de usuario en la consola");
    name = input("¿Como te llamas? :D ->");
    print(name.upper() , "tiene" , str(len(name)) , " letras");
    return name;
valor = nombre_usuario_consola();
print("Presiona enter para salir");
input();


""" Sin funcion """

print("Ingresa tu nombre de usuario en la consola");
name = input("¿Como te llamas? :D ->");
print(name.upper() , "tiene" , str(len(name)) , " letras");
print("Presiona enter para salir");
input();
