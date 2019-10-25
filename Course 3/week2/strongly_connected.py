#Uses python3

import sys

sys.setrecursionlimit(200000)

def postorder_dfs(v, t_adj, visited, res):
    visited[v] = True
    for neighbor in t_adj[v]:
        if visited[neighbor] == False:
            postorder_dfs(neighbor, t_adj, visited, res)
    res.append(v)

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

def explore(v, adj, visited):
    stack = [v]
    res = []
    while len(stack) != 0:
        top = stack.pop()
        res.append(top)
        visited[top] = True
        for child in adj[top]:
            if visited[child] == False:
                stack.append(child)
    return res

def number_of_strongly_connected_components(adj, t_adj):
    result = 0
    n = len(adj)
    visited = [False for _ in range(n)]
    stack = postorder_of_tansposed_graph(t_adj)
    while len(stack) != 0:
        top = stack.pop()
        if visited[top] == True:
            continue
        res = explore(top, adj, visited)
        result += 1
    return result

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
    print(number_of_strongly_connected_components(adj, t_adj))
