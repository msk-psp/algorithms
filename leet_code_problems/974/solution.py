from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        counter = 0
        dp = {0: 1}

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in dp:
                counter += dp[remainder]

            if not remainder in dp:
                dp[remainder] = 1
            else:
                dp[remainder] += 1
        return counter
