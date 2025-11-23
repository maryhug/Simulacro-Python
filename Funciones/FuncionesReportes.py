# ============= FUNCIONES DE REPORTES =============

import Datos as datos


def productos_mas_vendidos():
    """Muestra los 3 productos más vendidos"""
    print(f"\n{datos.SEPARADOR_PEQUENO}")
    print("TOP 3 PRODUCTOS MÁS VENDIDOS")
    print(datos.SEPARADOR_PEQUENO)

    if not datos.ventas:
        print("No hay Datos de ventas disponibles.")
        return

    # Contar cantidades vendidas por producto
    ventas_producto = {}

    for venta in datos.ventas:
        nombre_producto = venta['nombre_producto']
        cantidad = venta['cantidad']

        if nombre_producto in ventas_producto:
            ventas_producto[nombre_producto] += cantidad
        else:
            ventas_producto[nombre_producto] = cantidad

    # Ordenar por cantidad (descendente)
    productos_ordenados = sorted(ventas_producto.items(), key=lambda x: x[1], reverse=True)

    # Mostrar top 3
    if not productos_ordenados:
        print("No hay productos vendidos aún.")
        return

    for i, (producto, cantidad) in enumerate(productos_ordenados[:3], 1):
        print(f"{i}. {producto} - {cantidad} unidades vendidas")

    print(datos.SEPARADOR_PEQUENO)


def ventas_por_marca():
    """Muestra las ventas agrupadas por marca"""
    print(f"\n{datos.SEPARADOR_PEQUENO}")
    print("VENTAS POR MARCA")
    print(datos.SEPARADOR_PEQUENO)

    if not datos.ventas:
        print("No hay Datos de ventas disponibles.")
        return

    # Agrupar ventas por marca
    ventas_marca = {}

    for venta in datos.ventas:
        marca = venta['marca']
        total = venta['total']

        if marca in ventas_marca:
            ventas_marca[marca] += total
        else:
            ventas_marca[marca] = total

    # Mostrar resultados ordenados por nombre de marca
    if not ventas_marca:
        print("No hay Datos de marca disponibles.")
        return

    for marca, total in sorted(ventas_marca.items()):
        print(f"{marca}: ${total:.2f}")

    print(datos.SEPARADOR_PEQUENO)


def reporte_ingresos():
    """Muestra ingresos brutos y netos"""
    print(f"\n{datos.SEPARADOR_PEQUENO}")
    print("REPORTE DE INGRESOS")
    print(datos.SEPARADOR_PEQUENO)

    if not datos.ventas:
        print("No hay Datos de ventas disponibles.")
        return

    # Calcular usando funciones lambda
    ingresos_brutos = sum(map(lambda v: v['precio_unitario'] * v['cantidad'], datos.ventas))
    ingresos_netos = sum(map(lambda v: v['total'], datos.ventas))
    descuento_total = ingresos_brutos - ingresos_netos

    print(f"Ingresos brutos: ${ingresos_brutos:.2f}")
    print(f"Descuentos totales: ${descuento_total:.2f}")
    print(f"Ingresos netos: ${ingresos_netos:.2f}")

    # Métricas adicionales
    if ingresos_brutos > 0:
        porcentaje_descuento = (descuento_total / ingresos_brutos) * 100
        print(f"Descuento promedio: {porcentaje_descuento:.2f}%")

    print(f"Total de ventas: {len(datos.ventas)}")
    print(datos.SEPARADOR_PEQUENO)


def rendimiento_inventario():
    """Muestra el rendimiento del inventario basado en ventas"""
    print(f"\n{datos.SEPARADOR}")
    print("RENDIMIENTO DEL INVENTARIO")
    print(datos.SEPARADOR)

    if not datos.inventario:
        print("No hay Datos de inventario disponibles.")
        return

    # Calcular total vendido por producto
    vendido_por_producto = {}

    for venta in datos.ventas:
        codigo = venta['codigo_producto']
        cantidad = venta['cantidad']

        if codigo in vendido_por_producto:
            vendido_por_producto[codigo] += cantidad
        else:
            vendido_por_producto[codigo] = cantidad

    # Mostrar rendimiento
    valor_inventario_total = 0
    ingresos_generados_total = 0

    for codigo, producto in datos.inventario.items():
        vendido = vendido_por_producto.get(codigo, 0)
        ingresos = vendido * producto['precio']
        valor_inventario = producto['stock'] * producto['precio']

        valor_inventario_total += valor_inventario
        ingresos_generados_total += ingresos

        print(f"\n{producto['nombre']} ({codigo}):")
        print(f"  Stock actual: {producto['stock']} unidades")
        print(f"  Unidades vendidas: {vendido}")
        print(f"  Ingresos totales: ${ingresos:.2f}")
        print(f"  Valor del inventario: ${valor_inventario:.2f}")

        # Indicador de rendimiento
        if vendido == 0:
            print(f"  Estado: ⚠ Sin ventas aún")
        elif producto['stock'] < 5:
            print(f"  Estado: 🔴 Stock bajo - Considere reordenar")
        else:
            print(f"  Estado: ✓ Bueno")

    print(f"\n{datos.SEPARADOR}")
    print(f"Valor total del inventario: ${valor_inventario_total:.2f}")
    print(f"Ingresos totales generados: ${ingresos_generados_total:.2f}")
    print(datos.SEPARADOR)