def caixeiro_viajante_vizinho_proximo(cities, distance, start):
    visited = []
    total_distance = 0
    current_city = start
    start_index = cities.index(start)

    while len(visited) < len(cities):
        visited.append(current_city)
        current_index = cities.index(current_city)
        min_distance = float('inf')
        next_city = None

        for i, d in enumerate(distance[current_index]):
            if cities[i] not in visited and d < min_distance:
                min_distance = d
                next_city = cities[i]

        if next_city:
            total_distance += min_distance
            current_city = next_city
        else:
            break

    if len(visited) == len(cities):
        last_index = cities.index(visited[-1])
        total_distance += distance[last_index][start_index]
        visited.append(start)

    print("Rota mais curta:", " -> ".join(visited))
    print("Distância total:", total_distance)

cidades = ['A', 'B', 'C', 'D', 'E']
distancia = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]
start = "A"

caixeiro_viajante_vizinho_proximo(cidades, distancia, start)