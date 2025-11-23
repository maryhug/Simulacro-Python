# ============= MÓDULO DE DATOS =============
# Almacenamiento centralizado de Datos para el Sistema de Tienda Electrónica

# Estructuras de Datos globales
inventario = {}
ventas = []

# Tipos de cliente y sus descuentos
descuentos_cliente = {
    "regular": 0,
    "vip": 10,
    "mayorista": 15
}

# Rutas de archivos
ARCHIVO_INVENTARIO = "Datos/inventario.json"
ARCHIVO_VENTAS = "Datos/ventas.json"

# Constantes
SEPARADOR = "=" * 70
SEPARADOR_PEQUENO = "=" * 50