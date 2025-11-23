# ============= FUNCIONES DE GESTIÓN DE ARCHIVOS =============

import json
import os
import Datos


def asegurar_directorio_datos():
    """Crea el directorio 'Datos' si no existe"""
    os.makedirs("../Datos", exist_ok=True)


def cargar_datos():
    """Carga los Datos de inventario y ventas desde archivos JSON"""
    asegurar_directorio_datos()

    # Cargar inventario
    if os.path.exists(Datos.ARCHIVO_INVENTARIO):
        try:
            with open(Datos.ARCHIVO_INVENTARIO, 'r', encoding='utf-8') as archivo:
                Datos.inventario = json.load(archivo)
            print(f"✓ Cargados {len(Datos.inventario)} productos desde {Datos.ARCHIVO_INVENTARIO}")
        except json.JSONDecodeError as e:
            print(f"Error: Formato JSON inválido en archivo de inventario: {e}")
            Datos.inventario = {}
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            Datos.inventario = {}
    else:
        print(f"Archivo {Datos.ARCHIVO_INVENTARIO} no encontrado. Creando inventario inicial...")
        Datos.inventario = crear_inventario_inicial()
        guardar_inventario()

    # Cargar ventas
    if os.path.exists(Datos.ARCHIVO_VENTAS):
        try:
            with open(Datos.ARCHIVO_VENTAS, 'r', encoding='utf-8') as archivo:
                Datos.ventas = json.load(archivo)
            print(f"✓ Cargadas {len(Datos.ventas)} ventas desde {Datos.ARCHIVO_VENTAS}")
        except json.JSONDecodeError as e:
            print(f"Error: Formato JSON inválido en archivo de ventas: {e}")
            Datos.ventas = []
        except Exception as e:
            print(f"Error al cargar ventas: {e}")
            Datos.ventas = []
    else:
        print(f"Archivo {Datos.ARCHIVO_VENTAS} no encontrado. Iniciando con historial vacío.")
        Datos.ventas = []
        guardar_ventas()


def guardar_inventario():
    """Guarda el inventario en archivo JSON"""
    asegurar_directorio_datos()
    try:
        with open(Datos.ARCHIVO_INVENTARIO, 'w', encoding='utf-8') as archivo:
            json.dump(Datos.inventario, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar inventario: {e}")
        return False


def guardar_ventas():
    """Guarda las ventas en archivo JSON"""
    asegurar_directorio_datos()
    try:
        with open(Datos.ARCHIVO_VENTAS, 'w', encoding='utf-8') as archivo:
            json.dump(Datos.ventas, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar ventas: {e}")
        return False


def crear_inventario_inicial():
    """Crea y retorna el inventario inicial con 5 productos"""
    return {
        "P001": {
            "nombre": "Laptop HP",
            "marca": "HP",
            "categoria": "Computadoras",
            "precio": 850.00,
            "stock": 15,
            "garantia": 12
        },
        "P002": {
            "nombre": "Teléfono Samsung Galaxy",
            "marca": "Samsung",
            "categoria": "Teléfonos",
            "precio": 699.00,
            "stock": 25,
            "garantia": 24
        },
        "P003": {
            "nombre": "Audífonos Sony",
            "marca": "Sony",
            "categoria": "Audio",
            "precio": 149.00,
            "stock": 40,
            "garantia": 6
        },
        "P004": {
            "nombre": "Smart TV LG",
            "marca": "LG",
            "categoria": "Televisores",
            "precio": 1200.00,
            "stock": 10,
            "garantia": 18
        },
        "P005": {
            "nombre": "iPad Apple",
            "marca": "Apple",
            "categoria": "Tabletas",
            "precio": 499.00,
            "stock": 20,
            "garantia": 12
        }
    }