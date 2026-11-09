
from collections import deque

# ==========================================
# 1. DEFINICIÓN DEL GRAFO
# ==========================================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}


# ==========================================
# 2. ALGORITMO BFS
# ==========================================

def bfs(graph, start, target):

    # Inicializar estructuras
    queue = deque([start])
    discovered = {start}
    parent = {start: None}

    print("\n--- INICIO DE BFS ---")
    print("Cola inicial:", list(queue))
    print("Nodos descubiertos:", discovered)

    # Caso especial: inicio y destino son iguales
    if start == target:
        return parent

    # Mientras la cola no esté vacía
    while queue:

        # Extraer el primer nodo
        u = queue.popleft()

        print(f"\nProcesando nodo: {u}")

        # Recorrer vecinos en orden ascendente
        for v in sorted(graph[u]):

            print(f"  Revisando vecino: {v}")

            # Verificar si ya fue descubierto
            if v not in discovered:

                # Marcar como descubierto
                discovered.add(v)

                # Registrar su padre
                parent[v] = u

                # Agregar a la cola
                queue.append(v)

                print(f"    {v} agregado a discovered")
                print(f"    Padre de {v}: {u}")
                print(f"    Cola actual: {list(queue)}")

                # Comprobar si encontramos el destino
                if v == target:
                    print(f"\n¡Destino {target} encontrado!")
                    return parent

            else:
                print(f"    {v} ya fue descubierto. Se ignora.")

    return parent


# ==========================================
# 3. RECONSTRUCCIÓN DEL CAMINO
# ==========================================

def reconstruir_camino(parent, start, target):

    # Comprobar si el destino fue alcanzado
    if target not in parent:
        return None

    camino = []
    actual = target

    # Retroceder desde el destino hasta el inicio
    while actual is not None:
        camino.append(actual)
        actual = parent[actual]

    # Invertir para obtener inicio -> destino
    camino.reverse()

    return camino


# ==========================================
# 4. EJECUCIÓN DEL PROGRAMA
# ==========================================

if __name__ == "__main__":

    start = 'A'
    target = 'G'

    # Ejecutar BFS
    parent = bfs(graph, start, target)

    # Reconstruir camino
    camino = reconstruir_camino(parent, start, target)

    # Mostrar resultados
    print("\n========== RESULTADOS ==========")

    print("Nodo inicial:", start)
    print("Nodo destino:", target)

    print("\nRelación de padres:")
    for nodo, padre in parent.items():
        print(f"{nodo} <- {padre}")

    if camino:
        print("\nCamino encontrado:")
        print(" -> ".join(camino))
        print("Número de aristas:", len(camino) - 1)
    else:
        print("\nNo existe un camino entre los nodos.")

    print("\n================================")
