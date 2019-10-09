# Uses python3
import sys

def helper(arr, key, left, right):
    if right < left:
        return -1
    mid = int(left + (right - left) / 2)
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return helper(arr, key, mid+1, right)
    elif arr[mid] > key:
        return helper(arr, key, left, mid-1)

def binary_search(a, x):
    left, right = 0, len(a)-1
    return helper(a, x, left, right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')