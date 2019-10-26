#implement Bellman-Ford Algorithm
import math
def BellmanFord(edges, n):
    dist = [math.inf for _ in range(n)]
    prev = [i for i in range(n)]
    dist[0] = 0
    prev[0] = None
    for _ in range(n-1):
        for edge in edges:
            u, v, w = edge
            updated_dist = dist[u] + w
            if dist[v] > updated_dist:
                dist[v] = updated_dist
                prev[v] = u
    for edge in edges:
        u, v, w = edge
        if dist[v] > dist[u] + w:
            return 1
    return 0
    