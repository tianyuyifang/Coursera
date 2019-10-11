# Uses python3
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

# n = (len(str)-1)//2
# 0 <= i < j <= n
def MinAndMax(MinDp, MaxDp, str, i, j):
    MinDp[i][j] = sys.maxsize
    MaxDp[i][j] = -sys.maxsize-1
    for k in range(i, j):
        op = str[2*k+1]
        min1 = MinDp[i][k]
        max1 = MaxDp[i][k]
        min2 = MinDp[k+1][j]
        max2 = MaxDp[k+1][j]
        a = evalt(min1, min2, op)
        b = evalt(min1, max2, op)
        c = evalt(max1, min2, op)
        d = evalt(max1, max2, op)
        MinDp[i][j] = min(MinDp[i][j], a, b, c, d)
        MaxDp[i][j] = max(MaxDp[i][j], a, b, c, d)

def get_maximum_value(str):
    n = (len(str)-1)//2
    MinDp = [(n+1)*[None] for _ in range(n+1)]
    MaxDp = [(n+1)*[None] for _ in range(n+1)]
    for i in range(n+1):
        MinDp[i][i] = int(str[2*i])
        MaxDp[i][i] = int(str[2*i])
    # i + s = j
    for s in range(1, n+1):
        for i in range(0, n-s+1):
            j = i+s
            MinAndMax(MinDp, MaxDp, str, i, j)
    return MaxDp[0][n]

if __name__ == "__main__":
    print(get_maximum_value(input()))
