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

def dfs(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.append(next)
                remove_from_stack = False
                break
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