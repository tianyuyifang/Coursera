#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    queue = deque([s])
    n = len(adj)
    visited = [False for _ in range(n)]
    visited[s] = True
    dist = 0
    while len(queue) != 0:
        parameter = len(queue)
        for _ in range(parameter):
            cur = queue.popleft()
            if cur == t: 
                return dist
            for neighbor in adj[cur]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] = True
        dist += 1
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
