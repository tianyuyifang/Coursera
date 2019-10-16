# python3

def max_sliding_window_naive(sequence, m):
    n = len(sequence)
    maximums = []
    if n < m:
        return maximums
    max_queue = []
    for i in range(m):
        cur = sequence[i]
        while len(max_queue) != 0 and max_queue[-1] < cur:
            max_queue.pop()
        max_queue.append(cur)
    maximums.append(max_queue[0])
    for i in range(m, n):
        cur = sequence[i]
        while len(max_queue) != 0 and max_queue[-1] < cur:
            max_queue.pop()
        max_queue.append(cur)
        head = sequence[i-m]
        if max_queue[0] == head:
            max_queue.remove(head)
        maximums.append(max_queue[0])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

