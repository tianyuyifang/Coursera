#Uses python3
import sys
import math
class disjoint_set:
    def __init__(self, data):
        MAX = 1000
        self.size = len(data)
        #set parent and rank to be a list of size MAX
        self.parent = [None]*MAX
        self.rank = [None]*MAX
        for point in data:
            self.MakeSet(point)
    def MakeSet(self, value):
        self.parent[value] = value
        self.rank[value] = 0
        self.size += 1
    def Find(self, value):
        #consider the case where value is not in the sets
        if self.parent[value] == None:
            return "Not Found"
        paths = []
        while value != self.parent[value]:
            paths.append(value)
            value = self.parent[value]
        for node in paths:
            self.parent[node] = value
        return value
    def Union(self, v1, v2):
        id_1 = self.Find(v1)
        id_2 = self.Find(v2)
        if "Not Found" in [id_1, id_2]:
            return
        if id_1 == id_2:
            return
        rank_1 = self.rank[id_1]
        rank_2 = self.rank[id_2]
        if rank_1 > rank_2:
            self.parent[id_2] = id_1
        elif rank_2 > rank_1:
            self.parent[id_1] = id_2
        else:
            self.parent[id_1] = id_2
            self.rank[id_2] += 1  

def dist(i, j, x, y):
    xi = x[i]
    xj = x[j]
    yi = y[i]
    yj = y[j]
    return math.sqrt((xi-xj)*(xi-xj) + (yi-yj)*(yi-yj))

def produce_edges(x, y):
    n = len(x)
    edges = []
    for i in range(n-1):
        for j in range(i+1,n):
            edges.append((dist(i,j,x,y),i,j))
    return edges

def clustering(x, y, k):
    edges = produce_edges(x,y)
    n = len(x)
    ds = disjoint_set([i for i in range(n)])
    edges = sorted(edges)
    components = n
    for edge in edges:
        w, v1, v2 = edge
        if ds.Find(v1) != ds.Find(v2):
            ds.Union(v1, v2)
            components -= 1
            if components == k-1:
                return w

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
