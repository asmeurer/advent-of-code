# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def dijkstra(graph, start, end):
    unvisited = set(graph)
    dist = {node: float('inf') for node in unvisited}
    dist[start] = 0
    prev = {}

    while unvisited:
        current = min(unvisited, key=lambda i: dist[i])
        unvisited.remove(current)
        if current == end:
            break
        for node in graph[current]:
            if node in unvisited:
                alt = dist[current] + 1
                if alt < dist[node]:
                    dist[node] = alt
                    prev[node] = current

    path = []
    while current != start:
        path.insert(0, current)
        current = prev[current]

    return path
