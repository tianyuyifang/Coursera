# Uses python3
def edit_distance(s, t):
    len_s = len(s) + 1
    len_t = len(t) + 1
    maximum = len_t + len_s
    dp = [[maximum for col in range(len_t)] for row in range(len_s)]
    dp[0][0] = 0
    for i in range(1, len_s):
        dp[i][0] = i
    for j in range(1, len_t):
        dp[0][j] = j
    for j in range(1, len_t):
        for i in range(1, len_s):
            m1 = maximum
            if s[i-1] == t[j-1]:
                m1 = dp[i-1][j-1]
            m2 = dp[i-1][j] + 1
            m3 = dp[i][j-1] + 1
            m4 = dp[i-1][j-1] + 1
            dp[i][j] = min(m1, m2, m3, m4)
    return dp[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
