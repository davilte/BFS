import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

initial_vertice = "8"
adj_list = {
    "8": ["3"],
    "3": ["1", "2", "4"],
    "1": ["4"],
    "2": ["4"],
    "4": ["7", "6"],
    "6": ["7", "5"],
    "7": ["5"],
    "5": []
}
a = [(8, 3), (3, 1), (3, 2), (3, 4), (1, 4), (2, 4), (4, 7), (4, 6), (6, 7), (6, 5), (7, 5), (5, 0)]

# funcao com grafo e o no principal.
def dfs(graph, node):
    #adicionando o node que esta visitando e adicionando ele na pilha.
    visited = [node]
    stack = [node]

    while stack:
        #enquanto nao for vazia, continua.
        node = stack[-1]
        #adiciona o no visitado.
        if node not in visited:
            visited.append(node)
        remove_from_stack = True
        #passa o proximo a ser visitado.
        for next in graph[node]:
            if next not in visited:
                #adiciona o novo na pilha.
                stack.append(next)
                remove_from_stack = False
                #enquanto nao acabar os proximos, ela retorna na condicao.
                break

        #caso acabe os proximos, irar voltar e remover os visitados.    
        if remove_from_stack:
            stack.pop()
    return visited


print(dfs(adj_list, initial_vertice))

G = nx.Graph()
plt.figure(figsize=(18, 18))
G.add_edges_from(a)
nx.draw_networkx(
    G,
    node_size=15000,
    node_color='gray',
    font_size=15000//500
    )
plt.show()