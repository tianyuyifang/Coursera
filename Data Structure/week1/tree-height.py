# python3

import sys

def compute_height(parent):
    n = len(parent)
    visited = [False for _ in range(n)]
    height = 0
    for i in range(n):
        if visited[i] == True:
            continue
        cheight = 1
        while parent[i] != -1:
            visited[i] = True
            i = parent[i]
            cheight += 1
        height = max(height, cheight)
    return height

def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    print(compute_height(parent))

if __name__ == "__main__":
    main()
