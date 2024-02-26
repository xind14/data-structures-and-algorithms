from data_structures.queue import Queue

class Graph:
    def __init__(self):
        self.graph = {}

    def size(self):
        return len(self.graph)

    def add_node(self, value):
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.graph or node2 not in self.graph:
            raise KeyError

        self.graph[node1].append(Edge(node2, weight))


    def get_neighbors(self, node):
        return self.graph[node]


    def get_nodes(self):
        return self.graph.keys()

    def breadth_first(self, start_node):
        visited = set()
        result = []
        queue = Queue()

        queue.enqueue(start_node)
        visited.add(start_node)

        while not queue.is_empty():
            current_node = queue.dequeue()
            result.append(current_node.value)

            for neighbor in self.graph[current_node]:
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    queue.enqueue(neighbor.vertex)

        return result



class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight