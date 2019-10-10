# Uses python3
import sys

def maxiumValueOfTheLoot(capacity, weights, values):
    arr = [[x,y] for x,y in zip(values, weights)]
    sortArr = sorted(arr, key=lambda x: x[0]/x[1], reverse=True)
    v = 0
    while(capacity > 0 and len(sortArr)):
        value = sortArr[0][0]
        weight = sortArr[0][1]
        if capacity >= weight:
            v += value
            capacity -= weight
            sortArr = sortArr[1:]
        else:
            v += value*capacity/weight
            capacity = 0
    return v


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = maxiumValueOfTheLoot(capacity, weights, values)
    print("{:.10f}".format(opt_value))
