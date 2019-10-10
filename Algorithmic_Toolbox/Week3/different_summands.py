# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sum = 0
    i = 1
    while sum + i <= n:
        sum += i
        summands.append(i)
        i += 1
    if sum != n:
        summands[-1] = n-sum+i-1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
