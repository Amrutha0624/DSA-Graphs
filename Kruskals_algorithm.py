def compute_optimal_costs(graph):
    # Step 1: Set J(z) = 0 for the starting node
    optimal_costs = {node: float('inf') for node in graph}
    optimal_costs['z'] = 0  # Assuming 'z' is the starting node

    # Step 2: Iterate until all vertices have their optimal costs computed
    while any(cost == float('inf') for cost in optimal_costs.values()):
        for node in graph:
            # Skip if the optimal cost for the node is already computed
            if optimal_costs[node] != float('inf'):
                continue

            # Check if optimal cost for node can be computed
            neighbors = graph[node]
            if all(optimal_costs[neighbor] != float('inf') for neighbor in neighbors):
                # Compute optimal cost for the node using the formula
                optimal_costs[node] = min(
                    graph[node][neighbor] + optimal_costs[neighbor]
                    for neighbor in neighbors
                )

    return optimal_costs

# Example graph represented as an adjacency list
# Change the graph as per your requirements
example_graph = {
    'z': {'a': 2, 'b': 4},
    'a': {'c': 7},
    'b': {'c': 1},
    'c': {'d': 3},
    'd': {}
}

optimal_costs = compute_optimal_costs(example_graph)

# Print the optimal costs for each node
for node, cost in optimal_costs.items():
    print(f"Optimal cost for node {node}: {cost}")
