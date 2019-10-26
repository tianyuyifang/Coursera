#implement Prim's Algorithm

import heapq

def Prim(adj):
    included = [False for _ in range(len(adj))]
    included[0] = True
    heap = adj[0]
    heapq.heapify(heap)
    cost = 0
    while len(heap) != 0:
        #v1 is already included
        w, v1, v2 = heapq.heappop(heap)
        if included[v2] == True:
            continue
        included[v2] = True
        cost += w
        print(v1, "--", v2)
        for edge in adj[v2]:
            #if the edge is connected to an outside point
            if included[edge[2]] == False:
                heapq.heappush(heap, edge)
    return cost

#each edge is a tuple (weight ,point1, point2)
edges = [(1, 0, 1), (7, 0, 2), (5, 1, 2), (4, 1, 3), (6, 2, 4), (3, 1, 4), (2, 3, 4)]
n = 5
adj = [[] for _ in range(n)]
for edge in edges:
    w, v1, v2 = edge
    adj[v1].append((w, v1, v2))
    adj[v2].append((w, v2, v1))
cost = Prim(adj)
print(cost)