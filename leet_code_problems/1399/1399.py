class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 1   2   3   4   5   6   7   8   9
        # 10  11  12  13  14  15  16  17  18
        # 19  20  21  22  23  24

        group_sizes = {}

        for i in range(1, n + 1):
            current_num_str = str(i)
            digit_sum = sum(int(digit) for digit in current_num_str)

            group_sizes[digit_sum] = group_sizes.get(digit_sum, 0) + 1

        if not group_sizes:
            return 0
        
        max_size = max(group_sizes.values())

        count = 0

        for size in group_sizes.values():
            if size == max_size:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    # print(s.countLargestGroup(13))  # Output: 4
    # print(s.countLargestGroup(2))   # Output: 2
    # print(s.countLargestGroup(15))  # Output: 6
    print(s.countLargestGroup(24))  # Output: 5