# python3

import sys
from collections import deque

class Node:
    def __init__(self, index, children = []):
        self.index = index
        self.children = children
        
def print_children(node):
    if len(node.children) == 0:
        print("This node is a leaf")
    else:
        for child in node.children:
            print_node(child)

def print_node(node):
    print(node.index)


def read(parent):
    n = len(parent)
    nodes = [Node(i, []) for i in range(n)]
    for i in range(n):
        p = parent[i]
        if p == -1:
            root = nodes[i]
        else:
            nodes[p].children.append(nodes[i])
    return root
           
def compute_height_tree(root):
    q = deque()
    q.append(root)
    height = 0
    while True:
        size = len(q)
        if size == 0:
            break
        height += 1
        for _ in range(size):
            top = q.popleft()
            for child in top.children:
                q.append(child)
    return height



def compute_height(parent):
    if len(parent) == 0:
        return 0
    root = read(parent)
    return compute_height_tree(root)



def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    print(compute_height(parent))

if __name__ == "__main__":
    main()