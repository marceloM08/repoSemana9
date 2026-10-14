stack = []


def push(item, capacity):
    if not is_full(capacity):
        stack.append(item)
        return "Elemento apilado...."
    return "Fila llena..."

def isEmpty():
    return not len(stack)

def is_full(capacity):
    return len(stack) == capacity

def peek():
    if not isEmpty():
        return stack[-1]
    return "Pila vacía"


def pop():
    if not isEmpty():
        return stack.pop()
    return "Pila vacía..."

def show():
    message = ""
    for item in reversed(stack):
        message += f"| {item > 6}| \n"
        message += f"└" + "─"*8 + "┘\n"
    return message

capacity = int(input("Dime el tamaño de la pila: "))
while True:
    item = input("Dime un valor: ")
    print(push(item, capacity))
    answer = input("Desea ingresar otro dato [S | N]")
    if answer.lower() == "n":
        break

print("Mostrar tope")
print(peek())
print(peek())

print("Desapillar")
while True:
    answer = input("Desea desapillaar [S | N]: ")
    if answer.lower() == "si":
        print(pop())
    elif answer.lower() == "no":
        break
    else:
        print("opción Invalida....")