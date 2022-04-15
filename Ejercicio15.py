""" 15.	La jornada de trabajo es de 48 horas, calcular dada las horas 
trabajadas con el valor por hora. Mostrar su salario e indicar las horas extras si se 
excede de la j. """

def jornada():
    j = 48
    v = 15
    e = 20
    t = 60
    print(" horas trabajadas :")
    print (t)
    print(" La jornada es :")
    print (j, " horas")
    if(t > j):
        hte = t - j
        print (" horas trabajadas extras :")
        print (hte)
    else:
        print("No tiene horas extras")
    phe = e * hte
    print(" Pago de horas extras :")
    print (phe)
    pj = (j * v)+ phe
    print(" El pago por su jornada es :")
    print (pj, " dolares")
value = jornada();
print("Presiona Enter para salir :D");
input();

j = 48
v = 15
e = 20
t = 60
print(" horas trabajadas :")
print (t)
print(" La jornada es :")
print (j, " horas")
if(t > j):
   hte = t - j
   print (" horas trabajadas extras :")
   print (hte)
else:
   print("No tiene horas extras")
phe = e * hte
print(" Pago de horas extras :")
print (phe)
pj = (j * v)+ phe
print(" El pago por su jornada es :")
print (pj, " soles")