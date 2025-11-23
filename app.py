# ============= MENÚ PRINCIPAL =============

from Funciones.FuncionesArchivos import cargar_datos
from Funciones.FuncionesInventario import agregar_producto, actualizar_producto, eliminar_producto, mostrar_todos_productos
from Funciones.FuncionesVentas import registrar_venta, mostrar_historial_ventas
from Funciones.FuncionesReportes import reporte_ingresos, rendimiento_inventario, productos_mas_vendidos, ventas_por_marca

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("TIENDA DE ELECTRÓNICA - SISTEMA DE GESTIÓN")
    print("=" * 50)
    print("1. Mostrar todos los productos")
    print("2. Agregar nuevo producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Mostrar historial de ventas")
    print("7. Top 3 productos más vendidos")
    print("8. Ventas por marca")
    print("9. Reporte de ingresos")
    print("10. Rendimiento del inventario")
    print("0. Salir")
    print("=" * 50)

def principal():
    """Función principal - ejecuta el programa"""
    print("\n*** BIENVENIDO AL SISTEMA DE TIENDA DE ELECTRÓNICA ***")
    print("Cargando Datos desde archivos...")

    # Cargar Datos desde archivos al iniciar
    try:
        cargar_datos()
    except Exception as e:
        print(f"Error durante la inicialización: {e}")
        print("Iniciando con Datos vacíos...")

    while True:
        mostrar_menu()

        try:
            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                mostrar_todos_productos()
            elif opcion == "2":
                agregar_producto()
            elif opcion == "3":
                actualizar_producto()
            elif opcion == "4":
                eliminar_producto()
            elif opcion == "5":
                registrar_venta()
            elif opcion == "6":
                mostrar_historial_ventas()
            elif opcion == "7":
                productos_mas_vendidos()
            elif opcion == "8":
                ventas_por_marca()
            elif opcion == "9":
                reporte_ingresos()
            elif opcion == "10":
                rendimiento_inventario()
            elif opcion == "0":
                print("\n¡Gracias por usar el sistema. Hasta luego!")
                break
            else:
                print("⚠ Error: Opción inválida. Por favor seleccione un número del 0 al 10.")

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("¡Gracias por usar el sistema. Hasta luego!")
            break
        except Exception as e:
            print(f"⚠ Error inesperado: {e}")
            print("Por favor intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    principal()