# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    stack = []
    cur = 0
    while cur != -1:
        stack.append(cur)
        cur = self.left[cur]
    while len(stack) != 0:
        top = stack.pop()
        self.result.append(self.key[top])
        next = self.right[top]
        while next != -1:
            stack.append(next)
            next = self.left[next]       
    return self.result

  def preOrder(self):
    self.result = []
    stack = []
    stack.append(0)
    while len(stack) != 0:
      cur = stack.pop()
      right = self.right[cur]
      left = self.left[cur]
      self.result.append(self.key[cur])
      if right != -1:
        stack.append(right)
      if left != -1:
        stack.append(left)      
    return self.result

  def postOrder(self):
    self.result = []
    stack = []
    cur = 0
    while cur != -1:
        stack.append(cur)
        cur = self.left[cur]
    while len(stack) != 0:
        top = stack[-1]
        if top == "chao":
            stack.pop()
            top = stack.pop()
            self.result.append(self.key[top])
        elif self.right[top] == -1:
            top = stack.pop()
            self.result.append(self.key[top])
        else:
            stack.append("chao")
            next = self.right[top]
            while next != -1:
                stack.append(next)
                next = self.left[next]    
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

main()
# threading.Thread(target=main).start()