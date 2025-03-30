def caixeiro_viajante_vizinho_proximo(cities, distance):
    visited = []
    minimum_distance_traveled = []

    neighbor = 'A'
    start_node_index = cities.index(neighbor)

    no_nodes = len(cities)
    noN = 0
    while noN < no_nodes and neighbor not in visited:

        visited.append(neighbor)
        neighbor_index = cities.index(neighbor)
        noNeigjbour = 0
        MIN = 0

        while noNeigjbour < len(distance[neighbor_index]):
            if cities[noNeigjbour] not in visited:
                if MIN == 0:
                    MIN = distance[neighbor_index][noNeigjbour]
                    neighbor = cities[noNeigjbour]
                else:
                    min_distance = min(distance[neighbor_index][noNeigjbour], MIN)
                    if distance[neighbor_index][noNeigjbour] < MIN:
                        MIN = min_distance
                        neighbor = cities[noNeigjbour]
            noNeigjbour += 1
        minimum_distance_traveled.append(MIN)
        noN += 1
    last_node_index = cities.index(visited[-1])
    minimum_distance_traveled[-1] = distance[last_node_index][start_node_index]
    print('Rota mais curta : ', " -> ".join(visited))
    for _i in range(len(visited)):
        print("VIZINHO MAIS PRÓXIMO DE " + visited[_i] + " É ", minimum_distance_traveled[_i])
    print("DISTÂNCIA TOTAL", sum(minimum_distance_traveled))



cities = ['A', 'B', 'C', 'D', 'E']
distance = [[0, 0], [1, 5], [5, 2], [6, 6], [8, 3]]

caixeiro_viajante_vizinho_proximo(cities, distance)