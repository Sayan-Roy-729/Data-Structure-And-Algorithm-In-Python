"""
DIFFERENT GRAPH REPRESENTS:

# Edge List
graph1 = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent list (index of the array is the value of the actual graph node)
graph2 = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent matrix
graph3 = {
    0: [0, 0, 1, 0],
    1: [0, 0, 1, 1],
    2: [1, 1, 0, 1],
    3: [0, 1, 1, 0]
}
"""


class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        # undirected Graph
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(f"{node} --> {connections}")


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex("0")
    my_graph.add_vertex("1")
    my_graph.add_vertex("2")
    my_graph.add_vertex("3")
    my_graph.add_vertex("4")
    my_graph.add_vertex("5")
    my_graph.add_vertex("6")
    my_graph.add_edge("3", "1")
    my_graph.add_edge("3", "4")
    my_graph.add_edge("4", "2")
    my_graph.add_edge("4", "5")
    my_graph.add_edge("1", "2")
    my_graph.add_edge("1", "0")
    my_graph.add_edge("0", "2")
    my_graph.add_edge("6", "5")

    my_graph.show_connections()
