""" 14.	Escribir un script que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado 
redondeado con dos decimales. """

def peso():
    print("Ingresa los siguientes datos :D");
    weight = input("¿Cuál es tu peso en kg? ");
    height = input("¿Cuál es tu estatura en metros?");
    imc = round(float(weight)/float(height)**2,2);
    print("Tu índice de masa corporal es " + str(imc));
value = peso();
print("Presiona enter para salir :D");
input();

print("Ingresa los siguientes datos :D");
weight = input("¿Cuál es tu peso en kg? ");
height = input("¿Cuál es tu estatura en metros?");
imc = round(float(weight)/float(height)**2,2);
print("Tu índice de masa corporal es " + str(imc));
print("Presiona enter para salir :D");
input();