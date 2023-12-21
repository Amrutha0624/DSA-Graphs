INF = float('inf')
def floyd_algorithm(graph):
    num_vertices = len(graph)
    distance_matrix = [[INF] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distance_matrix[i][j] = 0
            elif graph[i][j] != 0:
                distance_matrix[i][j] = graph[i][j]
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance_matrix[i][k] != INF and distance_matrix[k][j] != INF:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    return distance_matrix
if __name__ == "__main__":
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    result = floyd_algorithm(graph)
    print("Shortest Distance Matrix:")
    for row in result:
        print(row)
