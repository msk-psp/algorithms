import heapq
import collections
from typing import List, Set, Dict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        inf = float("inf")

        minimum_ways = [[inf, 0] for n in range(n)]

        minimum_ways[0] = [0, 1]

        min_heap = [(0, 0)]

        visited = set()

        while min_heap:
            current_weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in graph[node]:
                if current_weight + weight < minimum_ways[neighbor][0]:
                    minimum_ways[neighbor][0] = current_weight + weight
                    minimum_ways[neighbor][1] = minimum_ways[node][1]

                elif current_weight + weight == minimum_ways[neighbor][0]:
                    minimum_ways[neighbor][1] += minimum_ways[node][1]

                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_weight + weight, neighbor))


        return minimum_ways[n-1][1] % (pow(10, 9) + 7)





if __name__ == "__main__":
    print(Solution().countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
    pass