# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    # (t, i) indicates that i-th worker will be free at 
    next_free_time = [(0, i) for i in range(n_workers)]
    heapq.heapify(next_free_time)
    for job in jobs:
        next_worker = heapq.heappop(next_free_time)
        t = next_worker[0]
        i = next_worker[1]
        result.append(AssignedJob(i, t))
        updated_worker = (t+job, i)
        heapq.heappush(next_free_time, updated_worker)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
