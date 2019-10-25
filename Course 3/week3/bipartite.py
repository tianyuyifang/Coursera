#Uses python3

import sys
from collections import deque

def scan(adj, v, colors):
    colors[v] = 1
    queue = deque()
    queue.append(v)
    while len(queue) != 0:
        top = queue.popleft()
        p_color = colors[top]
        for neighbor in adj[top]:
            n_color = colors[neighbor]
            if n_color == 0:
                queue.append(neighbor)
                colors[neighbor] = -1*p_color
            elif n_color == p_color:
                return False
    return True

def bipartite(adj):
    n = len(adj)
    colors = [0 for _ in range(n)]
    for v in range(n):
        if colors[v] == 0:
            if scan(adj, v, colors) == False:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
