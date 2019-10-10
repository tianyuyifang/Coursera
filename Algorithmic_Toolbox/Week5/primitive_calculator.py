# Uses python3
import sys
import math

def optimal_sequence(n):
    a = [math.inf]*(n+1)
    b = [1]*(n+1)
    a[0] = 0
    a[1] = 0
    minChanges = 1000000
    for i in range(2, n+1):
        if i % 3 == 0:
            mult3 = a[i//3] + 1
        else:
            mult3 = minChanges
        if i % 2 == 0:
            mult2 = a[i//2] + 1
        else:
            mult2 = minChanges
        minus1 = a[i-1] + 1

        a[i] = min(mult3, mult2, minus1)
        if a[i] == minus1:
            b[i] = i-1
        if a[i] == mult2:
            b[i] = i//2
        if a[i] == mult3:
            b[i] = i//3
    sequence = []
    while n != 1:
        sequence.append(n)
        n = b[n]
    sequence.append(1)
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
