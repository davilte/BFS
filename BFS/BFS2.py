from queue import Queue

vertices = ["R", "S", "T", "U", "V", "W", "X", "Y"]
adj_list = {
    "R": ["S", "V"],
    "S": ["W", "R"],
    "T": ["U", "W", "X"],
    "U": ["T", "X", "Y"],
    "V": ["R"],
    "W": ["S", "T", "X"],
    "X": ["T", "U", "W", "Y"],
    "Y": ["U", "X"]
}
j = -1

def BFS(initialVertice):
    # armazenamos todos os nós visitados
    visited = {}

    # armazenamos o nível de cada dicionário (a distância)
    level = {}

    # armazenamos o pai de cada nó
    parent = {}

    # armazenamos a ordem da BFS
    bfs_traversal_output = []

    # iniciamos uma lista vazia
    queue = Queue()

    # percorremos todos os nós do dicionario
    for node in adj_list.keys():
        # inicializando todos sem visita, sem pai e sem level
        visited[node] = False
        parent[node] = None
        level[node] = -1

    # aqui definimos nosso nó inicial, visitamos ele, definimos seu nivel (que como é o primeiro é 0) e adicionamos na lista
    s = initialVertice
    visited[s] = True
    level[s] = 0
    queue.put(s)

    # enquanto a lista temporária não for vazia
    while not queue.empty():
        # remove e armazena o primeiro elemento da lista temporária
        u = queue.get()

        # e adiciona na final da lista pra ficar em ordem
        bfs_traversal_output.append(u)

        # e pra cada vizinho do vertice
        for v in adj_list[u]:
            # checamos se ele ja foi visitado, caso não...
            if not visited[v]:
                # visitamos ele
                visited[v] = True

                # definimos seu pai (u)
                parent[v] = u

                # dizemos que a distancia dele é 1 a mais que a de seu pai
                level[v] = level[u] + 1

                # e adicionamos ele na lista temporária para fazermos o mesmo com seus vizinhos
                queue.put(v)

    
    aux = j

    # while aux != 0:
    #     # print(aux)
    #     level[vertices[aux]] = 0
    #     print(level)
    #     aux -= 1

    # level[vertices[j]] = 0
    print(level)

    a = sum(level.values())
    return a

dist = 0
for i in vertices:
    dist = dist + BFS(i)
    j += 1

averageDist = dist / len(vertices)

print(dist)
print(averageDist)