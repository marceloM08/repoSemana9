Pile = []

def push(item, capacity):
    if not is_full(capacity):
        Pile.append(item)
        return "Caja apilada..."
    return "Pila llena..."

def isEmpty():
    return len(Pile) == 0

def is_full(capacity):
    return len(Pile) == capacity

def peek():
    if not isEmpty():
        return Pile[-1]
    return "Pila vacía"

def pop():
    if not isEmpty():
        return Pile.pop()
    return "Pila vacía..."

def show():
    if isEmpty():
        return "La pila está vacía..."
    message = ""
    for item in reversed(Pile):
        message += f"| {item} |\n"
        message += f"└" + "─"*8 + "┘\n"
    return message

def menu(capacity):
    while True:
        print("\n--- MENÚ ---")
        print("1. Apilar caja")
        print("2. Desapilar caja")
        print("3. Consultar tope")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            item = input("Ingrese la caja a apilar: ")
            print(push(item, capacity))

        elif opcion == "2":
            print("Caja desapilada:", pop())

        elif opcion == "3":
            print("Caja en el tope:", peek())

        elif opcion == "4":
            print("Contenido de la pila:\n", show())

        elif opcion == "5":
            print("\n--- RESUMEN FINAL ---")
            print(f"Cantidad de cajas en la pila: {len(Pile)}")
            if isEmpty():
                print("La pila quedó vacía.")
            else:
                print("La pila aún tiene cajas:", Pile)
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


capacidad = int(input("Ingrese la capacidad máxima de la pila: "))
menu(capacidad)
