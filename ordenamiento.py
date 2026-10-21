# ordenamiento.py

def obtener_indices_ordenados(lista_codigos: list) -> list:
    """Ordenamiento por inserción sobre arreglos auxiliares de índices para mantener sincronizados los arreglos paralelos"""
    indices = list(range(len(lista_codigos)))
    for i in range(1, len(indices)):
        actual = indices[i]
        j = i - 1
        while j >= 0 and lista_codigos[indices[j]] > lista_codigos[actual]:
            indices[j + 1] = indices[j]
            j -= 1
        indices[j + 1] = actual
    return indices

def busqueda_binaria_expediente(codigos_ordenados: list, codigo_buscado: str) -> int:
    """Algoritmo de Búsqueda Binaria O(log n) sobre el arreglo de códigos de expediente"""
    bajo = 0
    alto = len(codigos_ordenados) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if codigos_ordenados[medio] == codigo_buscado:
            return medio
        elif codigos_ordenados[medio] < codigo_buscado:
            bajo = medio + 1
        else:
            alto = medio - 1
            
    return -1  # Retorna -1 si no se encuentra el código


# Bloque de pruebas independientes para ver resultados en la terminal
if __name__ == "__main__":
    print("--- PRUEBAS DEL MÓDULO ORDENAMIENTO Y BÚSQUEDA ---")
    
    # Datos de prueba simulados
    codigos_prueba = ["EXP-003", "EXP-001", "EXP-005", "EXP-002"]
    print(f"Códigos originales: {codigos_prueba}")
    
    # 1. Probar ordenamiento por índices
    indices = obtener_indices_ordenados(codigos_prueba)
    codigos_ordenados = [codigos_prueba[i] for i in indices]
    print(f"Códigos ordenados: {codigos_ordenados}")
    
    # 2. Probar búsqueda binaria
    buscado = "EXP-003"
    posicion = busqueda_binaria_expediente(codigos_ordenados, buscado)
    
    if posicion != -1:
        print(f"¡Éxito! El código '{buscado}' fue encontrado en la posición ordenada #{posicion}.")
    else:
        print(f"El código '{buscado}' no fue encontrado.")