# =====================================================================
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# Solución al Problema 3: Auditoría de Inventario
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) encargado de determinar la cantidad exacta 
    de artículos a solicitar según las reglas del negocio.
    """
    # Si el Stock Actual es menor al Stock Mínimo, se calcula la diferencia
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    # Si el Stock Actual es suficiente, la cantidad a pedir es cero
    else:
        return 0

def generar_informe_pedidos(matriz_inventario):
    """
    Módulo encargado de recorrer la matriz de inventario, procesar
    cada artículo e imprimir el listado final de pedidos.
    """
    print("==================================================")
    print("        INFORME DE PEDIDOS - REABASTECIMIENTO     ")
    print("==================================================")
    print(f"{'ARTÍCULO':<25} | {'CANTIDAD A PEDIR':<15}")
    print("-" * 50)
    
    # Recorrer la matriz fila por fila (cada artículo)
    for articulo in matriz_inventario:
        # Extraer los datos según el formato de la matriz
        # [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
        nombre_articulo = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamar a la función para calcular la cantidad exacta a solicitar
        cantidad_solicitada = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Imprimir el nombre del artículo y la cantidad exacta que debe ser solicitada
        print(f"{nombre_articulo:<25} | {cantidad_solicitada:<15}")
        
    print("==================================================")

# Programa Principal (Punto de entrada)
if __name__ == "__main__":
    # Matriz inicial con 5 artículos (Código, Nombre, Stock Actual, Stock Mínimo Requerido)
    inventario_tienda = [
        ["ART001", "Cuadernos Universitarios", 12, 20],
        ["ART002", "Bolígrafos Tinta Negra", 45, 30],
        ["ART003", "Marcadores Resaltadores", 4, 15],
        ["ART004", "Carpetas Archivadoras", 8, 8],
        ["ART005", "Calculadoras Científicas", 2, 10]
    ]
    
    # Ejecución de la funcionalidad principal
    generar_informe_pedidos(inventario_tienda)