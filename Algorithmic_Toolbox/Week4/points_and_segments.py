# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    adjusted_starts = [(i,-1) for i in starts]
    adjusted_ends = [(i,1) for i in ends]
    adjusted_points = [(i, 0) for i in points]
    all_points = sorted(adjusted_ends + adjusted_points + adjusted_starts)
    cnt = dict()
    cur = 0
    for point in all_points:
        state = point[1]
        number = point[0]
        if state == -1:
            cur += 1
        elif state == 0:
            cnt[number] = cur
        else:
            cur -= 1
    res = []
    for i in points:
        res.append(cnt[i])
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
