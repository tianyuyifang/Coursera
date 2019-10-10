# Uses python3
import sys

def get_change(m):
    a = (m+1)*[0]
    a[0] = 0
    a[1] = 1
    minChanges = 1000
    for i in range(2, m+1):
        if i >= 4:
            minus4 = a[i-4] + 1
        else:
            minus4 = minChanges
        if i >= 3:
            minus3 = a[i-3] + 1
        else:
            minus3 = minChanges
        minus1 = a[i-1] + 1
        a[i] = min(minus4, minus3, minus1)
    return a[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
