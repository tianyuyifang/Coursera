# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        if src_parent == dst_parent:
            return False
        src_rank = self.ranks[src]
        dst_rank = self.ranks[dst]
        final_count = self.row_counts[src_parent] + self.row_counts[dst_parent]
        if src_rank < dst_rank:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] = final_count
        elif src_rank > dst_rank:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] = final_count
        else:
            self.parents[src_parent] = dst_parent
            self.ranks[dst_parent] += 1
            self.row_counts[dst_parent] = final_count
        self.max_row_count = max(final_count, self.max_row_count)
        return True

    def get_parent(self, table):
        # find parent and compress path
        paths = []
        while table != self.parents[table]:
            paths.append(table)
            table = self.parents[table]
        for node in paths:
            self.parents[node] = table
        return table


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
