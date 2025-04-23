from typing import *

def find(parent, x):
    if parent[x - 1] != x:
        return find(parent, parent[x - 1])
    return x

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b - 1] = a
    else:
        parent[a - 1] = b


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n + 1 for n in range(len(edges))]

        for node1, node2 in edges:
            if find(parent, node1) == find(parent, node2):
                return [node1, node2]
            union(parent, node1, node2)


if __name__ == "__main__":
    print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    pass









