#Uses python3
import sys
import math
import heapq

def dist(i, j, x, y):
    xi = x[i]
    xj = x[j]
    yi = y[i]
    yj = y[j]
    return math.sqrt((xi-xj)*(xi-xj) + (yi-yj)*(yi-yj))

def minimum_distance(x, y):
    included = [False for _ in range(len(x))]
    included[0] = True
    heap = []
    for i in range(1,len(x)):
        heapq.heappush(heap, (dist(0,i,x,y), 0, i))
    cost = 0
    while len(heap) != 0:
        #v1 is already included
        w, v1, v2 = heapq.heappop(heap)
        if included[v2] == True:
            continue
        included[v2] = True
        cost += w
        for v in range(len(x)):
            #if the edge is connected to an outside point
            if included[v] == False:
                heapq.heappush(heap, (dist(v2,v,x,y),v2,v))
    return cost


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
