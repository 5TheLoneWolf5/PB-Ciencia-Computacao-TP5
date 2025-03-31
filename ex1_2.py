import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def min_key(self, key, mstSet):
        min_val = sys.maxsize
        min_index = None

        for vertex in key:
            if key[vertex] < min_val and not mstSet[vertex]:
                min_val = key[vertex]
                min_index = vertex

        return min_index

    def prim_mst(self):
        key = {vertex: sys.maxsize for vertex in self.graph}
        parent = {vertex: None for vertex in self.graph}
        mstSet = {vertex: False for vertex in self.graph}

        start_node = next(iter(self.graph))
        key[start_node] = 0
        parent[start_node] = None

        for _ in range(len(self.graph)):
            u = self.min_key(key, mstSet)
            if u is None:
                break

            mstSet[u] = True

            for neighbor, weight in self.graph[u]:
                if not mstSet[neighbor] and key[neighbor] > weight:
                    key[neighbor] = weight
                    parent[neighbor] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Aresta \tPeso")
        for node in parent:
            if parent[node] is not None:
                print(f"{parent[node]} - {node} \t {self.get_weight(parent[node], node)}")

    def get_weight(self, u, v):
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return None

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 4)
    g.add_edge("C", "D", 5)

    g.prim_mst()
