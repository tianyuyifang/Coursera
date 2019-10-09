# Uses python3
import sys


def isMajority(key, a, left, right):
    cnt = 0
    for x in a[left:right]:
        if x == key:
            cnt += 1
    return True if cnt > (right-left)/2 else False
      
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left+1 ==  right:
        return a[left]
    mid = int(left + (right-left)/2)
    leftMajority = get_majority_element(a, left, mid)
    rightMajority = get_majority_element(a, mid, right)
    if isMajority(leftMajority, a, left, right):
        return leftMajority
    elif isMajority(rightMajority, a, left, right):
        return rightMajority
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
