# ============= FUNCIONES DE INVENTARIO =============

from Funciones.FuncionesArchivos import guardar_inventario
import Datos

def obtener_float_valido(mensaje, valor_minimo=0):
    """Función auxiliar para obtener entrada flotante válida"""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < valor_minimo:
                print(f"Error: El valor debe ser al menos {valor_minimo}")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def obtener_int_valido(mensaje, valor_minimo=0):
    """Función auxiliar para obtener entrada entera válida"""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < valor_minimo:
                print(f"Error: El valor debe ser al menos {valor_minimo}")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")

def obtener_entrada_no_vacia(mensaje):
    """Función auxiliar para obtener entrada de texto no vacía"""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede estar vacío.")

def mostrar_todos_productos():
    """Muestra todos los productos en el inventario"""
    print(f"\n{Datos.SEPARADOR}")
    print("INVENTARIO ACTUAL")
    print(Datos.SEPARADOR)

    if not Datos.inventario:
        print("No hay productos en el inventario.")
        return

    for codigo, producto in Datos.inventario.items():
        print(f"\nCódigo: {codigo}")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Marca: {producto['marca']}")
        print(f"  Categoría: {producto['categoria']}")
        print(f"  Precio: ${producto['precio']:.2f}")
        print(f"  Stock: {producto['stock']} unidades")
        print(f"  Garantía: {producto['garantia']} meses")
    print(Datos.SEPARADOR)

def agregar_producto():
    """Agrega un nuevo producto al inventario"""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")

    try:
        codigo = obtener_entrada_no_vacia("Código del producto (ej: P006): ").upper()

        if codigo in Datos.inventario:
            print("Error: ¡Este código ya existe!")
            return

        nombre = obtener_entrada_no_vacia("Nombre del producto: ")
        marca = obtener_entrada_no_vacia("Marca: ")
        categoria = obtener_entrada_no_vacia("Categoría: ")
        precio = obtener_float_valido("Precio: $", valor_minimo=0.01)
        stock = obtener_int_valido("Cantidad en stock: ", valor_minimo=0)
        garantia = obtener_int_valido("Garantía (meses): ", valor_minimo=0)

        Datos.inventario[codigo] = {
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "garantia": garantia
        }

        if guardar_inventario():
            print(f"✓ Producto '{nombre}' agregado y guardado exitosamente!")
        else:
            print("⚠ Producto agregado pero no se pudo guardar en el archivo.")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def actualizar_producto():
    """Actualiza un producto existente"""
    print("\n--- ACTUALIZAR PRODUCTO ---")

    if not Datos.inventario:
        print("No hay productos en el inventario para actualizar.")
        return

    codigo = input("Ingrese el código del producto a actualizar: ").strip().upper()

    if codigo not in Datos.inventario:
        print("Error: Producto no encontrado.")
        return

    producto = Datos.inventario[codigo]
    print(f"\nProducto actual: {producto['nombre']}")
    print("Deje en blanco para mantener el valor actual")

    try:
        nombre = input(f"Nuevo nombre [{producto['nombre']}]: ").strip()
        if nombre:
            producto['nombre'] = nombre

        precio_entrada = input(f"Nuevo precio [${producto['precio']:.2f}]: ").strip()
        if precio_entrada:
            precio = float(precio_entrada)
            if precio > 0:
                producto['precio'] = precio
            else:
                print("Advertencia: El precio debe ser positivo. Manteniendo valor actual.")

        stock_entrada = input(f"Nuevo stock [{producto['stock']}]: ").strip()
        if stock_entrada:
            stock = int(stock_entrada)
            if stock >= 0:
                producto['stock'] = stock
            else:
                print("Advertencia: El stock no puede ser negativo. Manteniendo valor actual.")

        if guardar_inventario():
            print("✓ Producto actualizado y guardado exitosamente!")
        else:
            print("⚠ Producto actualizado pero no se pudo guardar en el archivo.")

    except ValueError:
        print("Error: Entrada inválida. Actualización cancelada.")
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")

def eliminar_producto():
    """Elimina un producto del inventario"""
    print("\n--- ELIMINAR PRODUCTO ---")

    if not Datos.inventario:
        print("No hay productos en el inventario para eliminar.")
        return

    codigo = input("Ingrese el código del producto a eliminar: ").strip().upper()

    if codigo not in Datos.inventario:
        print("Error: Producto no encontrado.")
        return

    nombre_producto = Datos.inventario[codigo]['nombre']
    confirmacion = input(f"¿Está seguro de eliminar '{nombre_producto}'? (si/no): ").lower()

    if confirmacion in ['si', 's', 'sí']:
        del Datos.inventario[codigo]
        if guardar_inventario():
            print(f"✓ Producto '{nombre_producto}' eliminado y guardado exitosamente!")
        else:
            print("⚠ Producto eliminado pero no se pudo guardar en el archivo.")
    else:
        print("Eliminación cancelada.")