productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para la cantidad.")
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    if not productos:
        print("No hay productos para mostrar.")
        return
    for idx, producto in enumerate(productos):
        print(f"{idx + 1}: {producto['nombre']} - Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    if not productos:
        return
    while True:
        try:
            idx = int(input("Selecciona el número del producto a actualizar: ")) - 1
            if idx < 0 or idx >= len(productos):
                raise IndexError
            break
        except (ValueError, IndexError):
            print("Por favor, selecciona un número válido.")
    
    nombre = input("Introduce el nuevo nombre del producto (dejar en blanco para no cambiar): ")
    if nombre:
        productos[idx]['nombre'] = nombre
    
    while True:
        try:
            precio = input("Introduce el nuevo precio del producto (dejar en blanco para no cambiar): ")
            if precio:
                productos[idx]['precio'] = float(precio)
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")
    
    while True:
        try:
            cantidad = input("Introduce la nueva cantidad del producto (dejar en blanco para no cambiar): ")
            if cantidad:
                productos[idx]['cantidad'] = int(cantidad)
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para la cantidad.")

    print("Producto actualizado con éxito.")

def eliminar_producto():
    ver_productos()
    if not productos:
        return
    while True:
        try:
            idx = int(input("Selecciona el número del producto a eliminar: ")) - 1
            if idx < 0 or idx >= len(productos):
                raise IndexError
            break
        except (ValueError, IndexError):
            print("Por favor, selecciona un número válido.")
    
    eliminado = productos.pop(idx)
    print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")

def guardar_datos():
    with open("productos.txt", "w") as f:
        for producto in productos:
            f.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as f:
            for line in f:
                nombre, precio, cantidad = line.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt. Se comenzará con una lista vacía.")
    except ValueError:
        print("Error en el formato de los datos del archivo. Asegúrate de que sean correctos.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
