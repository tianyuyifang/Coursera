#Uses python3

import sys

def explore(x, adj, visited, order):
    visited[x] = True
    for v in adj[x]:
        if visited[v] == False:
            explore(v, adj, visited, order)
    order.append(x)
    return

def toposort(adj):
    n = len(adj)
    visited = [False for _ in range(n)]
    order = []
    for v in range(n):
        if visited[v] == False:
            explore(v, adj, visited, order)
    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

