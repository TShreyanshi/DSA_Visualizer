class Node:
    """Represents a single vertex in a graph or tree."""

    def __init__(self, value):
        self.value = value
        self.visited = False      # used in BFS/DFS traversal

    def __repr__(self):
        return f"Node({self.value})"


class Graph:
    """Adjacency list graph — works for both directed and undirected."""

    def __init__(self, directed=False):
        self.adjacency_list = {}   # { node_value: [neighbor_values] }
        self.directed = directed

    def add_vertex(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = []

    def add_edge(self, from_val, to_val, weight=1):
        self.add_vertex(from_val)
        self.add_vertex(to_val)
        self.adjacency_list[from_val].append((to_val, weight))
        if not self.directed:
            self.adjacency_list[to_val].append((from_val, weight))

    def __repr__(self):
        return f"Graph({self.adjacency_list})"