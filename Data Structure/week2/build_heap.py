# python3


def sift_down(data, i):
    n = len(data)
    swaps = []
    while 2*i+1 <= n-1 :
        smallest_index = i
        if data[smallest_index] > data[2*i+1]:
            smallest_index = 2*i+1
        if 2*i+2 <= n-1 and data[smallest_index] > data[2*i+2]:
            smallest_index = 2*i+2
        if smallest_index == i:
            break
        else:
            data[i], data[smallest_index] = data[smallest_index], data[i]
            swaps.append([i, smallest_index])
            i = smallest_index
    return swaps

def sift_up(data, i):
    swaps = []
    while i!= 0:
        parent = (i-1)//2
        if data[i] < data[parent]:
            data[i], data[parent] = data[parent], data[i]
            swaps.append([parent, i])
            i = parent
        else:
            break
    return swaps

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    for i in range((n-1)//2, -1, -1):
        swap = sift_down(data, i)
        swaps += swap
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
