from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]

        visit = set()

        t = 0

        while min_heap:

            w1, n1 = heapq.heappop(min_heap)

            if n1 in visit:
                continue

            visit.add(n1)

            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visit) == n else -1
        # start = k
        # total_cost = 0
        #
        # networks = [] * (n - 1)
        #
        # for index in range(n):
        #     networks.append([math.inf] * n)
        #
        # max_time = math.inf
        #
        # for time in times:
        #     source = time[0]
        #     target = time[1]
        #     time_cost = time[2]
        #
        #     networks[source - 1][target - 1] = time_cost
        #
        # visited = {start}
        #
        # stack = [start]
        #
        # current_time = 0
        #
        # paths = networks[start - 1]
        #
        # while True:
        #     inner_stack = stack
        #     stack = []
        #     for node in inner_stack:
        #         for neighbor, time_cost in enumerate(networks[node - 1]):
        #             if time_cost == math.inf:
        #                 continue
        #
        #             if neighbor + 1 not in visited:
        #                 if current_time >= time_cost:
        #                     visited.add(neighbor + 1)
        #                     stack.append(neighbor + 1)
        #                 else:
        #                     stack.append(node)
        #     if len(stack) == 0:
        #         break
        #     total_cost += 1
        #     # current_time += 0
        #
        #
        # if len(visited) == n:
        #     return total_cost
        # else:
        #     return -1


if __name__ == "__main__":
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2)
    print(Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2) == 3)
    print(Solution().networkDelayTime([[1,2,1],[2,3,2]], 3, 1))
    pass




