""" 11.	Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde el prefijo 
es el código del país +503, y la extensión tiene dos dígitos (por ejemplo
+503-913724710-56). Escribir un script que pregunte por un número de teléfono con este formato y 
muestre por pantalla el número de teléfono sin el prefijo y la extensión.(solamente el número 
de teléfono)
 """

def telefono():
    telefono = input("Ingresa tu numero de telefonocon con el formato +503-7087-8104->");
    print("El numero de telefono es: ", telefono[4:12]);
value = telefono();
print("Presiona enter para salir");
input();


telefono = input("Ingresa tu numero de telefonocon con el formato +503-7087-8104->");
print("El numero de telefono es: ", telefono[4:12]);
print("Presiona enter para salir");
input();