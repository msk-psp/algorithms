from typing import *

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        grid_size = len(grid)
        subgrid_size = grid_size // 2

        if subgrid_size == 0:
            return Node(grid[0][0], True, None, None, None, None)

        top_left = [top[:subgrid_size] for top in grid[:subgrid_size]]
        top_right = [top[subgrid_size:] for top in grid[:subgrid_size]]
        bottom_left = [bottom[:subgrid_size] for bottom in grid[subgrid_size:]]
        bottom_right = [bottom[subgrid_size:] for bottom in grid[subgrid_size:]]

        if subgrid_size == 1 and top_left[0][0] == top_right[0][0] == bottom_left[0][0] == bottom_right[0][0]:
            return Node(top_left[0][0], True, None, None, None, None)

        node_top_left = self.construct(top_left)
        node_top_right = self.construct(top_right)
        node_bottom_left = self.construct(bottom_left)
        node_bottom_right = self.construct(bottom_right)

        if node_top_left.val == node_top_right.val == node_bottom_left.val == node_bottom_right.val and node_top_left.isLeaf and node_top_right.isLeaf and node_bottom_left.isLeaf and node_bottom_right.isLeaf:
            return Node(node_top_left.val, True, None, None, None, None)
        else:
            return Node(1, False, node_top_left, node_top_right, node_bottom_left, node_bottom_right)


if __name__ == "__main__":
    grid = [
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 0]
          ]

    node = Solution().construct(grid)

    node = Solution().construct([
        [1,1,0,0],
        [0,0,1,1],
        [1,1,0,0],
        [0,0,1,1]
    ])

    print(node)