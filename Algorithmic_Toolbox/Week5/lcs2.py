#Uses python3

import sys

def lcs2(a, b):
    len_a = len(a) + 1
    len_b = len(b) + 1
    dp = [[0] * (len_b) for _ in range(len_a)]
    for j in range(1, len_b):
        for i in range(1, len_a):
            m1 = 0
            if a[i-1] == b[j-1]:
                m1 = dp[i-1][j-1] + 1
            m2 = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = max(m1, m2)
    return dp[len(a)][len(b)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
