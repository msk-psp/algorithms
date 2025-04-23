from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # find a case that prefix_sum - nums[i] equals to k
        # https://seing.tistory.com/125

        prefix_sum = 0
        occurrence = 0
        dp = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in dp:
                occurrence += dp[prefix_sum - k]

            if prefix_sum not in dp:
                dp[prefix_sum] = 1
            else:
                dp[prefix_sum] = dp[prefix_sum] + 1

        return occurrence














        # if len(nums) == 1:
        #     return 1 if nums[0] == k else 0
        #
        # while True:
        #     if cumulated < k and right < len(nums):
        #         cumulated += nums[right]
        #         right += 1
        #     # elif cumulated > k:
        #     else:
        #         cumulated -= nums[left]
        #         left += 1
        #
        #     if cumulated == k:
        #         # cumulated -= nums[left]
        #         # left += 1
        #         array_nums += 1
        #
        #     if left == right == len(nums):
        #         break
        #
        # return array_nums




        # while True:
        #     if cumulated < k:
        #         num = nums[right]
        #         cumulated += num
        #         right += 1
        #     # elif cumulated > k:
        #     else:
        #         cumulated -= nums[left]
        #         left += 1
        #
        #     if cumulated == k:
        #         array_nums += 1
        #         right += 1
        #         # cumulated -= nums[left]
        #         # left += 1
        #
        #     if left == right:
        #         break
        # return array_nums

if __name__ == "__main__":
    print(Solution().subarraySum([10, 20, 30, 40, 50, 60, 10, 60, 70, 20, 20, 30], 70))

    print(Solution().subarraySum([-1, -1, 1], 0))
    print(Solution().subarraySum([1], 0))
    print(Solution().subarraySum([1], 1))
    print(Solution().subarraySum([1, 2, 3], 3))
    print(Solution().subarraySum([1, 1, 1], 2) == 2)
    print(Solution().subarraySum([4,2,5,1,7,2,3,1], 15) == 2)
    print(Solution().subarraySum([1, 1, 1, 1, 7, 2, 3, 1], 3) == 3)