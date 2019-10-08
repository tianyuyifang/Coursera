# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    p1 = l
    p2 = l
    p3 = r 
    while( p2 < p3 ):
        i = p2 + 1
        if a[i] == x:
            p2 += 1
        elif a[i] < x:
            a[p1], a[i] = a[i], a[p1]
            p2 += 1
            p1 += 1
        else:
            a[p3], a[i] = a[i], a[p3]
            p3 -= 1
    return p1, p2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    p1, p2 = partition3(a, l, r)
    randomized_quick_sort(a, l, p1 - 1);
    randomized_quick_sort(a, p2 + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
