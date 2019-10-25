#Uses python3

import sys

def postorder_dfs(v, t_adj, visited, res):
    visited[v] = True
    for neighbor in t_adj[v]:
        if visited[neighbor] == False:
            postorder_dfs(neighbor, t_adj, visited, res)
    res.append(v)
    return

def postorder_of_tansposed_graph(t_adj):
    postorder = []
    n = len(t_adj)
    visited = [False for _ in range(n)]
    for v in range(n):
        if visited[v] == False:
            res = []
            postorder_dfs(v, t_adj, visited, res)
            postorder += res
    return postorder

def acyclic(adj, t_adj):
    stack = postorder_of_tansposed_graph(t_adj)
    n = len(adj)
    visited = [False for _ in range(n)]
    while len(stack) != 0:
        top = stack.pop()
        visited[top] = True
        for v in adj[top]:
            if visited[v] == False:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    t_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        t_adj[b - 1].append(a - 1)
    print(acyclic(adj, t_adj))
