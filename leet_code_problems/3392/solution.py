class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for middle_index in range(1, len(nums) - 1):
            left = nums[middle_index - 1]
            middle = nums[middle_index]
            right = nums[middle_index + 1]

            if left + right == middle / 2:
                count += 1

        return count

            


        


        