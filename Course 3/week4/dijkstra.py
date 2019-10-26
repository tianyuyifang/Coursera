#Uses python3

import sys
import heapq

def distance(adj, cost, s, t):
    dist = [float('inf') for _ in range(len(adj))]
    dist[s] = 0
    #heap is a min heap with priority to be the distance and value to be the point
    #each time heap pops the point with the least distance which must be 
    heap = [(0,s)]
    while len(heap) != 0:
        d, v = heapq.heappop(heap)
        #if dist[v] > d, the tuple (v,d) is invalid, keep poping
        #Valid tuple should always satisfy that dist[v] == d
        if dist[v] > d:
            continue
        if v == t:
            return dist[t]
        for i in range(len(adj[v])):
            next_v = adj[v][i]
            weight = cost[v][i]
            updated_dist = d + weight
            if dist[next_v] > updated_dist:
                dist[next_v] = updated_dist
                heapq.heappush(heap, (updated_dist, next_v))
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
