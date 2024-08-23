inventario = []

def menu_principal():
    """
    Muestra el menú principal.
    """
    while True:
        print("Menú Principal")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Vender Producto")
        print("4. Actualizar Stock")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, intente otra vez.")
            
def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    
    inventario.append(producto)
    
    print(f"Producto '{nombre}' agregado al inventario.")

def mostrar_inventario():
    """
    Muestra todos los productos del inventario.
    """
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['stock']}")

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta.
    """
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input(f"¿Cuántas unidades de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venta realizada. Total: ${total:.2f}")
                
                if producto["stock"] == 0:
                    print(f"El producto '{nombre}' se ha agotado.")
                    
                return
            else:
                print("No hay suficiente stock en inventario.")
                return
    print("Producto no encontrado en el inventario.")

def actualizar_stock():
    """
    Actualiza la cantidad de stock de un producto determinado.
    """
    nombre = input("Ingrese el nombre del producto cuyo stock desea actualizar: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            while True:
                cantidad = input(f"Ingrese la nueva cantidad de stock para '{nombre}': ")
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    producto["stock"] = cantidad
                    print(f"Stock para '{nombre}' actualizado a {cantidad}.")
                    return
                else:
                    print("La cantidad debe ser un número entero. Inténtelo de nuevo.")
    
    print("Producto no encontrado en el inventario.")

menu_principal()

