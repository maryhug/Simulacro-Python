# ============= FUNCIONES DE VENTAS =============

from Funciones.FuncionesArchivos import guardar_inventario, guardar_ventas
from datetime import datetime
import Datos


def registrar_venta():
    """Registra una nueva venta"""
    print("\n--- REGISTRAR NUEVA VENTA ---")

    if not Datos.inventario:
        print("Error: No hay productos en el inventario. Agregue productos primero.")
        return

    # Verificar si hay productos con stock
    productos_disponibles = {codigo: prod for codigo, prod in Datos.inventario.items() if prod['stock'] > 0}

    if not productos_disponibles:
        print("Error: No hay productos con stock disponible.")
        return

    try:
        # Obtener información del cliente
        cliente = input("Nombre del cliente: ").strip()
        if not cliente:
            print("Error: El nombre del cliente no puede estar vacío.")
            return

        print("\nTipos de cliente:")
        print("1. Regular (0% descuento)")
        print("2. VIP (10% descuento)")
        print("3. Mayorista (15% descuento)")

        opcion_tipo = input("Seleccione tipo de cliente (1-3): ").strip()

        mapa_tipo_cliente = {
            "1": "regular",
            "2": "vip",
            "3": "mayorista"
        }

        if opcion_tipo not in mapa_tipo_cliente:
            print("Error: Tipo de cliente inválido.")
            return

        tipo_cliente = mapa_tipo_cliente[opcion_tipo]

        # Mostrar productos disponibles
        print("\nProductos disponibles:")
        for codigo, producto in productos_disponibles.items():
            print(f"  {codigo}: {producto['nombre']} - ${producto['precio']:.2f} ({producto['stock']} disponibles)")

        # Obtener producto
        codigo_producto = input("\nIngrese el código del producto: ").strip().upper()

        if codigo_producto not in Datos.inventario:
            print("Error: Producto no encontrado.")
            return

        producto = Datos.inventario[codigo_producto]

        if producto['stock'] == 0:
            print("Error: Este producto no tiene stock disponible.")
            return

        # Obtener cantidad
        try:
            cantidad = int(input("Cantidad a vender: "))
        except ValueError:
            print("Error: Por favor ingrese un número entero válido para la cantidad.")
            return

        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0.")
            return

        if cantidad > producto['stock']:
            print(f"Error: Stock insuficiente. Solo hay {producto['stock']} unidades disponibles.")
            return

        # Calcular precios
        porcentaje_descuento = Datos.descuentos_cliente[tipo_cliente]
        precio_unitario = producto['precio']
        subtotal = precio_unitario * cantidad
        monto_descuento = subtotal * (porcentaje_descuento / 100)
        total = subtotal - monto_descuento

        # Actualizar stock
        producto['stock'] -= cantidad

        # Registrar venta
        venta = {
            "cliente": cliente,
            "tipo_cliente": tipo_cliente,
            "codigo_producto": codigo_producto,
            "nombre_producto": producto['nombre'],
            "marca": producto['marca'],
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "porcentaje_descuento": porcentaje_descuento,
            "total": total,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Datos.ventas.append(venta)

        # Guardar tanto inventario como ventas
        inventario_guardado = guardar_inventario()
        ventas_guardadas = guardar_ventas()

        # Mostrar recibo
        print(f"\n{Datos.SEPARADOR_PEQUENO}")
        print("RECIBO DE VENTA")
        print(Datos.SEPARADOR_PEQUENO)
        print(f"Cliente: {cliente} ({tipo_cliente.upper()})")
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio unitario: ${precio_unitario:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento ({porcentaje_descuento}%): -${monto_descuento:.2f}")
        print(f"TOTAL: ${total:.2f}")
        print(f"Fecha: {venta['fecha']}")
        print(Datos.SEPARADOR_PEQUENO)

        if inventario_guardado and ventas_guardadas:
            print("✓ Venta registrada y guardada exitosamente!")
        else:
            print("⚠ Venta registrada pero hubo problemas al guardar en los archivos.")

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def mostrar_historial_ventas():
    """Muestra todas las ventas realizadas"""
    print(f"\n{Datos.SEPARADOR}")
    print("HISTORIAL DE VENTAS")
    print(Datos.SEPARADOR)

    if not Datos.ventas:
        print("No hay ventas registradas aún.")
        return

    ingresos_totales = 0
    for i, venta in enumerate(Datos.ventas, 1):
        print(f"\nVenta #{i}")
        print(f"  Cliente: {venta['cliente']} ({venta['tipo_cliente']})")
        print(f"  Producto: {venta['nombre_producto']}")
        print(f"  Cantidad: {venta['cantidad']}")
        print(f"  Total: ${venta['total']:.2f}")
        print(f"  Fecha: {venta['fecha']}")
        ingresos_totales += venta['total']

    print(f"\n{Datos.SEPARADOR}")
    print(f"Ingresos Totales: ${ingresos_totales:.2f}")
    print(Datos.SEPARADOR)