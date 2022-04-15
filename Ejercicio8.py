""" 8.La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
Escribir un script que pregunte al usuario si quiere una pizza vegetariana o no, y en 
función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y 
el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza 
elegida es vegetariana o no y todos los ingredientes que lleva.
 """

""" Con funcion """
def Pizzeria_Bella_Napoli():
    print("Bienvenidos a la pizzeria Bella Napoli ofrecemos pizas vegetaraianas y no vegetarianas-> presiona 1 si quieres vegetarianas | presiona 2 si quieres no vegetariana");
    pizza = input("Ingresa el numero del tipo de pizza que quieres ya sea 1 o 2 :D ->");
    if pizza == "1":
        print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
        ingredientes = input("Ingresa el tipo de ingredientes que deseas :D ->")
        print("Pizza vegetariana con mozarella, tomate y ", end="")
        if ingredientes == "1":
            print("Pimiento")
        else:
            print("Tofu")
    else:
        print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n");
        ingredientes = input("Ingresa el ingredente que deseas :D ->")
        print("Pizza no vegetariana con mozarella tomate y ", end="")
        if ingredientes == "1":
            print("peperoni")
        elif ingredientes == "2":
            print("jamon")
        else:
            print("Salmon")
valor = Pizzeria_Bella_Napoli();
print("Gracias por tu compra vuelva pronto de parte de PIZZERIA BELLA NAPOLI :D");
input();


""" Sin funcion """
print("Bienvenidos a la pizzeria Bella Napoli ofrecemos pizas vegetaraianas y no vegetarianas-> presiona 1 si quieres vegetarianas | presiona 2 si quieres no vegetariana");
pizza = input("Ingresa el numero del tipo de pizza que quieres ya sea 1 o 2 :D ->");
if pizza == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingredientes = input("Ingresa el tipo de ingredientes que deseas :D ->")
    print("Pizza vegetariana con mozarella, tomate y ", end="")
    if ingredientes == "1":
            print("Pimiento")
    else:
            print("Tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n");
    ingredientes = input("Ingresa el ingredente que deseas :D ->")
    print("Pizza no vegetariana con mozarella tomate y ", end="")
    if ingredientes == "1":
        print("peperoni")
    elif ingredientes == "2":
        print("jamon")
    else:
        print("Salmon")
print("Gracias por tu compra vuelva pronto de parte de PIZZERIA BELLA NAPOLI :D");
input();