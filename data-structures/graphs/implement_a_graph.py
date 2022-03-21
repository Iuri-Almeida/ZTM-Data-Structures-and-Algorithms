class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def __repr__(self):
        arr = []
        for k, v in self.adjacent_list.items():
            arr.append(f"{k} --> {', '.join(v)}")
        return "\n".join(arr)

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node_1, node_2):
        keys = self.adjacent_list.keys()
        if node_1 not in keys or node_2 not in keys:
            raise IndexError("First node not in the graph.")
        self.adjacent_list[node_1].append(node_2)
        self.adjacent_list[node_2].append(node_1)


my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')
print(my_graph)
