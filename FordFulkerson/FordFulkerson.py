# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # BFS como algoritimo de busca
    def BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Ford Fulkerson
    def ford_fulkerson(self, origem, destino):
        parent = [-1] * (self.ROW)
        max_flow = 0
        # Enquanto percorre pelo BFS
        while self.BFS(origem, destino, parent):
            path_flow = float("Inf")
            s = destino
            while(s != origem):
                # print(s)
                # print(self.graph[parent[s]][s])
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adicionando os fluxos de caminho
            max_flow += path_flow
            print(path_flow)

            # Atualizando os valores residuais dos nós
            v = destino
            while(v != origem):
                # print(v)
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 16, 13, 0, 0, 0], #A 0
        [0, 0, 10, 12, 0, 0], #B 1
        [0, 4, 0, 0, 14, 0], #C 2 
        [0, 0, 9, 0, 0, 20], #D 3
        [0, 0, 0, 7, 0, 4], #E 4
        [0, 0, 0, 0, 0, 0]] #F 5

g = Graph(graph)

origem = 1
destino = 5

print("Max Flow: %d" % g.ford_fulkerson(origem, destino))