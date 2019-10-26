#Uses python3

import sys

def negative_cycle(edges, n):
    dist = [10000000 for _ in range(n)]
    prev = [i for i in range(n)]
    dist[0] = 0
    prev[0] = None
    for _ in range(n-1):
        for edge in edges:
            u, v, w = edge
            #script starts from 0 while input starts from 1
            u = u - 1
            v = v - 1
            updated_dist = dist[u] + w
            if dist[v] > updated_dist:
                dist[v] = updated_dist
                prev[v] = u
    for edge in edges:
        u, v, w = edge
        u = u - 1
        v = v - 1
        if dist[v] > dist[u] + w:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(3 * m):3], data[1:(3 * m):3], data[2:(3 * m):3]))
    data = data[3 * m:]
    print(negative_cycle(edges, n))
