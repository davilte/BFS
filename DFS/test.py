# Biblioteca para desenho
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, label: any, value: float = float("inf")):
        self.label = str(label)
        self.value = value
        self.connections = []
        self.is_checked = False
        self.next = None

    def __str__(self):
        return f"{self.label}({self.value})"

class Graph:
    def __init__(self):
        self.nodes = []
        self.distance_to_root = 0

    def add_node(self, new_node: Node):
        if new_node in self.nodes:
            return

        self.nodes.append(new_node)

    def __str__(self):
        return ', '.join(str(n) for n in self.nodes)

    def get_all_connections(self):
        connections = []
        for i in self.nodes:
            for j in i.connections:
                arr = [str(i), str(j)]
                arr.sort()
                if arr not in connections:
                    connections.append(arr)

        return connections

    def start(self, node_root: str):
        root = None

        for node in self.nodes:
            if node.label == node_root:
                root = node

        # Verificar se encontrou um nó no grafo
        if type(root) == Node:
            self.unmark_all()
            root.value = 0
            self.recursive_dfs(root)
            self.draw_graph_from_graph(self)

    def unmark_all(self):
        for node in self.nodes:
            node.value = float("inf")

    def recursive_dfs(self, no: Node):
        no.is_checked = True
        no.value = self.distance_to_root

        for child in no.connections:
            if child.is_checked:
                continue

            self.distance_to_root += 1
            child.value = self.distance_to_root
            self.recursive_dfs(child)

    @staticmethod
    # Método para desenhar grafo a partir de um objeto "Graph"
    def draw_graph_from_graph(graph, node_color='orange', node_size=10000):
        draw_graph = []
        for i in graph.nodes:
            for j in i.connections:
                draw_graph.append([str(i), str(j)])

        Graph.draw_graph_from_arr(draw_graph, node_color, node_size)

    @staticmethod
    # Método para desenhar grafo a partir de uma lista de adjacências
    def draw_graph_from_arr(arr: list[list[any, any]], node_color='orange', node_size=10000):
        G = nx.Graph()
        plt.figure(figsize=(20, 20))
        G.add_edges_from(arr)
        nx.draw_networkx(
            G,
            node_size=node_size,
            node_color=node_color,
            font_size=node_size // 500
        )
        plt.show()


def setup_question(input_graph: Graph):
    nodes = {str(i + 1): [] for i in range(8)}

    nodes['3'] = ['1', '4']
    nodes['1'] = ['2']
    nodes['2'] = ['5', '6']
    nodes['5'] = ['6', '10', '9']
    nodes['6'] = ['10']
    nodes['9'] = []
    nodes['10'] = []
    nodes['4'] = ['1', '7', '8']
    nodes['7'] = ['11', '12']
    nodes['8'] = []
    nodes['11'] = []
    nodes['12'] = []

    all_nodes = dict((node, Node(node)) for node in nodes)

    for node in all_nodes:
        all_nodes[node].connections = [all_nodes[c] for c in nodes[node]]
        input_graph.add_node(all_nodes[node])


if __name__ == '__main__':
    g = Graph()
    setup_question(g)

    g.start('3')