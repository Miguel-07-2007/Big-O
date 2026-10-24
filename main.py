import random
import time

# ==========================================
# 1. ALGORITMO MERGE SORT (Divide y Vencerás)
# ==========================================

def merge_sort(lista):
    """
    Función recursiva de Merge Sort.
    Complejidad Temporal: O(n log n)
    Complejidad Espacial: O(n)
    """
    # CASO BASE: Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # 1. DIVIDIR: Punto medio para separar la lista
    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]
    
    # 2. VENCER: Ordenamiento recursivo de cada mitad
    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)
    
    # 3. COMBINAR: Mezcla ordenada de ambas sublistas
    return fusionar(izquierda_ordenada, derecha_ordenada)

def fusionar(izquierda, derecha):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    Costo temporal lineal: O(n)
    """
    resultado = []
    i = 0  # Puntero lista izquierda
    j = 0  # Puntero lista derecha
    
    # Comparar elementos de ambas sublistas e insertar el menor
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# ==========================================
# 2. DEMOSTRACIÓN PRÁCTICA DE BIG-O
# ==========================================

def medir_tiempo(n):
    # Generar una lista aleatoria de 'n' elementos
    lista = [random.randint(1, 1000000) for _ in range(n)]
    
    # Medición de tiempo de ejecución
    inicio = time.time()
    merge_sort(lista)
    fin = time.time()
    
    return fin - inicio

if __name__ == "__main__":
    print("==========================================")
    print("  DEMOSTRACIÓN DE COMPLEJIDAD O(n log n)  ")
    print("==========================================")
    print(f"{'Tamaño de entrada (n)':<22} | {'Tiempo (segundos)':<20}")
    print("-" * 50)
    
    # Evaluamos cómo escala el tiempo al aumentar 'n'
    tamanios = [1000, 10000, 100000, 500000]
    
    for n in tamanios:
        tiempo = medir_tiempo(n)
        print(f"{n:<22,} | {tiempo:<20.4f}")
        
    print("-" * 50)
    print("Observación: Al aumentar n por un factor de 10, el tiempo crece de forma O(n log n).")
