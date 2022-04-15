""" 1.	Si A = 9, B = 8 y C = 2, evaluar las siguientes expresiones:
a)	B * A - B * B / 4 * C	Resultado = 40
b)	(A * B) / 3 * 3	Resultado = 72
c) B + C / 2 * A + 10 * 3 * B – 6	Resultado = 1314
d) 40/5 * 5+6/2 * 3+4-5 * 2/10	Resultado = 52 
f) 4 / 2 * 3 / 6 + 6 / 2 / 1 / 5 mod 2 / 4 * 2	Resultado = 1.30
 """

""" Con funcion """
""" Literal a: """
def expresion1(a, b, c):
    a = 9;
    b = 8;
    c = 2;
    result = b * a - b * b / 4 * c
    return result
valor = expresion1(9, 8, 2);
print("El resultado de esta expresion 1 es: ", valor);

""" Sin funcion """
a = 9;
b = 8;
c = 2;
result = b * a - b * b / 4 * c
print("El resultado de esta expresion 1 es: ", result);

""" Con funcion """
""" Literal b: """
def expresion2(a, b):
    a = 9;
    b = 8;
    resultado = (a * b) / 3 * 3;
    return resultado;
valor = expresion2(9, 8);
print("El resultado de la expresion 2 es: ", valor);

""" Sin funcion """
a = 9;
b = 8;
resultado = (a * b) / 3 * 3;
print("El resultado de la expresion 2 es: ", resultado);

""" Con funcion """
""" Literal c: """
def expresion3(a, b, c):
    a = 9;
    b = 8;
    c = 2;
    results = b + c / 2 * a + 10 * 3 * b - 6;
    return results;
value = expresion3(9, 8, 2);
print("El resultado de la expresion 3 es: ", value);

""" Sin funcion """
a = 9;
b = 8;
c = 2;
results = b + c / 2 * a + 10 * 3 * b - 6;
print("El resultado de la expresion 3 es: ", results);

""" Con funcion """
""" Literal d: """
def expresion4():
    resultado = 40/5 * 5+6/2 * 3+4-5 * 2/10;
    return resultado;
value = expresion4();
print("El resultado de esta expresion 4 es: ", value);

""" Sin funcion """
resultado = 40/5 * 5+6/2 * 3+4-5 * 2/10;
print("El resultado de esta expresion 4 es: ", resultado);

""" Con funcion """
""" Literal f: """
def expresion5():
    resultado = 4 / 2 * 3 / 6 + 6 / 2 / 1 / 5 % 2 / 4 * 2;
    return resultado;
value = expresion5();
print("El resultado de la expresion 5 es: ", value);

""" Sin funcion """
resultado = 4 / 2 * 3 / 6 + 6 / 2 / 1 / 5 % 2 / 4 * 2;
print("El resultado de la expresion 5 es: ", resultado);

print("BY: Edgar :D presiona Enter para salir")
input()
