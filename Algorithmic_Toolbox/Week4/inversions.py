# Uses python3
import sys

def merge(a, b, left, right):
    ave = (left + right) // 2
    l = left
    r = ave
    num = 0
    for i in range(left, right ):
        if l != ave and r != right:
            if a[l] <= a[r]:
                b[i] = a[l]
                l += 1
            else:
                b[i] = a[r]
                num += ave - l
                r += 1
        elif l == ave:
            b[i] = a[r]
            r += 1
        else:
            b[i] = a[l]
            l += 1
    a[left:right] = b[left:right]
    return num
        
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, right)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
