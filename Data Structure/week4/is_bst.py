#!/usr/bin/python3

import sys, threading, math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if len(tree) == 0:
    return True
  keys = [x[0] for x in tree]
  left = [x[1] for x in tree]
  right = [x[2] for x in tree]
  stack = []
  cur = 0
  prev = -1*math.inf
  while cur != -1:
    stack.append(cur)
    cur = left[cur]
  while len(stack) != 0:
    top = stack.pop()
    if prev >= keys[top]:
      return False
    prev = keys[top]
    next = right[top]
    while next != -1:
      stack.append(next)
      next = left[next]
  return True
def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
