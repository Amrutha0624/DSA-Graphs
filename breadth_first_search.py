class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)

# Example usage:
# Create a directed graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Perform BFS starting from vertex 2
print("BFS starting from vertex 2:")
graph.bfs(2)
