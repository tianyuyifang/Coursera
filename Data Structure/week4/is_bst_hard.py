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
  while cur != -1:
    if right[cur] != -1:
      stack.append((cur, "r"))
    else:
      stack.append((cur, "l"))
    cur = left[cur]
  while len(stack) != 0:
    top = stack.pop()
    value = keys[top[0]]
    _type = top[1]
    _next = right[top[0]]
    while _next != -1:
      if right[_next] != -1:
        stack.append((_next, "r"))
      else:
        stack.append((_next, "l"))
      _next = left[_next]
    if len(stack) != 0:
      real_next = stack[-1][0]
      if (_type == "r" and value > keys[real_next]) or (_type == "l" and value >= keys[real_next]):
        return False
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

main()

# threading.Thread(target=main).start()
