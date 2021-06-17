# 9.1
graph = {
    'u': {'v': 2, 'x': 1, 'w': 5},
    'v': {'u': 2, 'x': 2, 'w': 3},
    'w': {'x': 3, 'y': 1, 'v': 3, 'z': 5},
    'x': {'v': 2, 'u': 1, 'y': 1, 'w': 3},
    'y': {'w': 1, 'x': 1, 'z': 2},
    'z': {'y': 2, 'w': 5}
}

# 9.2
# graph = {
#     'a': {'b': 5, 'c': 7, 'd': 1},
#     'b': {'c': 2},
#     'c': {'e': 5, 'd': 6},
#     'd': {'b': 3, 'g': 3, 'f': 5},
#     'e': {'f': 4},
#     'f': {'c': 1},
#     'g': {'e': 1}
# }

# 9.3
# graph = {
#     'a': {'e': 5, 'f': 1, 'l': 2},
#     'b': {'c': 11, 'i': 9},
#     'c': {'f': 3, 'j': 6, 'g': 5, 'd': 3},
#     'd': {'n': 5},
#     'e': {'h': 8, 'b': 1},
#     'f': {'i': 6, 'm': 4},
#     'g': {'d': 4, 'f': 1},
#     'h': {'m': 7},
#     'i': {'h': 10},
#     'j': {'k': 13, 'l': 8},
#     'k': {},
#     'l': {},
#     'm': {'k': 9},
#     'n': {'k': 6}
# }

def dijkstra(graph, start, goal):
    # Armazenará a menor distância para cada nó
    shortest_distance = {}

    # Encontrará a menor distância, quando for atualizado dirá de onde veio o caminho (se for de a -> b, o predecessor de b é a)
    predecessor = {}

    # Inicialmente será o nosso grafo, e rodará ele até ser todo visitado
    unseenNodes = graph

    infinity = 999999

    # Mostrará percurso no final
    path = []
    
    # Definir a menor distância de todos os nós (menos o inicial) para infinito
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # Enquanto ainda tiver algo dentro de unseenNodes
    while unseenNodes:
        minNode = None

        # Por ser um algorítmo guloso, temos que conferir se ele tem a menor distância possível
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        # Checar todos os filhos do nó
        for childNode, weight in graph[minNode].items():

            # Caso a soma do peso do nó filho com a distância do nó minimo for menor que a distância mínima do nó filho
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                
                # Trocamos o nó da distância mínima por essa soma
                shortest_distance[childNode] = weight + shortest_distance[minNode]

                # Definimos seu predecessor pra poder encontrar o caminho futuramente
                predecessor[childNode] = minNode

        # E vamos retirando o minNode até parar o loop
        unseenNodes.pop(minNode)

    # E para encontrar o caminho vamos percorrer de tras pra frente e armazenar cada passo até chegar no começo
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Caminho inalcançável")
            break
    path.insert(0, start)

    # Se for infinito é porque não foi alcançado, então se ele for alcançado printará o resultado
    if shortest_distance[goal] != infinity:
        print('Menor distancia: ' + str(shortest_distance[goal]))
        print('Caminho: ' + str(path))

dijkstra(graph, 'y', 'z')