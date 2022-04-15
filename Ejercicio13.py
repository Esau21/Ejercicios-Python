""" 13.	Escribir un script que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde. """

def hrs():
    print("Por favor queremos saber tus horas de trabajo y cual es tu paga :D");
    hors = float(input("Ingresa tus horas de trabajo :D ->"));
    cost = float(input("Ingresa cual es tu paga :D ->$"));
    pay = hors * cost;
    print("tu paga por horas de es: ", "$" , pay);
value = hrs();
print("Presiona para salir :D");
input();


print("Por favor queremos saber tus horas de trabajo y cual es tu paga :D");
hors = float(input("Ingresa tus horas de trabajo :D ->"));
cost = float(input("Ingresa cual es tu paga :D ->$"));
pay = hors * cost;
print("tu paga por horas de es: ", "$" , pay);
print("Presiona para salir :D");
input();

