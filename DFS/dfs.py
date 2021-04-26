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

# w: nao visitado | g: visitado | b: todos os vertices adjacentes visitados
color = {}

# armazenamos o pai de cada nó
parent = {}

# armazenamos o tempo de quando começa e quando termina em cada nó [start, end]
trav_time = {}

# armazenamos a ordem da DFS
dfs_traversal_output = []

# inicializando todas as dicts
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

dfs_util(initial_vertice)
print("\nOrdem DFS: ", dfs_traversal_output)
print("\nPais: ", parent)

print("\nÁrvore de profundidade: ")
for node in adj_list.keys():
    print(node, " -> ", trav_time[node])
    
# print("Taversal time: ", trav_time)
# print(color)

