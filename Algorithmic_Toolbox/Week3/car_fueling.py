# python3
import sys


def compute_min_refills(distance, tank, stops):
    minum = 0
    stops[:0] = [0]
    stops.append(distance)
    size = len(stops)
    c = 0
    n = 0
    while(c != size-1):
        while(n < size-1 and stops[n+1]-stops[c]<=tank):
            n += 1
        if c == n: 
            return -1 
        minum += 1
        c = n
    return minum-1

compute_min_refills(950, 400, [200,375,550,750])

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
