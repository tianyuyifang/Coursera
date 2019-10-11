# Uses python3
import sys

def optimal_weight(Capacity, weights):
    n = len(weights) + 1
    dp = [n*[0] for _ in range(Capacity + 1)]
    for W in range(1, Capacity + 1):
        for i in range(1, n):
            #if weights i is not part of optimal knapsack
            dp[W][i] = dp[W][i-1]
            weights_i = weights[i-1]
            if W >= weights_i:
                dp[W][i] = max(dp[W][i], dp[W-weights_i][i-1] + weights_i)
    return dp[Capacity][len(weights)]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
