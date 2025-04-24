from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Calculate the required number of distinct elements for a subarray to be complete.
        target_len = len(set(nums))

        # Initialize the total count of complete subarrays found.
        count = 0
        # Initialize the left boundary (start index) of the sliding window.
        start = 0
        # Get the total length of the input array for calculations.
        n = len(nums)
        # Dictionary to store the frequency of each element within the current window [start...end].
        window_counts = {}

        # Iterate through the array with 'end' representing the right boundary of the window.
        for end in range(n):
            # Expand the window to the right by including the element nums[end].
            # Update its frequency count in our window map.
            window_counts[nums[end]] = window_counts.get(nums[end], 0) + 1
            
            # Check if the current window [start...end] is now complete.
            # If it is, try shrinking it from the left while maintaining completeness.
            while len(window_counts) == target_len:
                # If window [start...end] is complete, all subarrays starting at 'start'
                # and ending at 'end' or later (i.e., nums[start...end], nums[start...end+1], ..., nums[start...n-1])
                # are also complete. There are (n - end) such subarrays. Add them to the count.
                count += (n - end)
                
                # Try to shrink the window from the left:
                # Decrement the count of the element at the 'start' index.
                window_counts[nums[start]] -= 1
                # If the count of this element drops to zero, remove it from the map
                # as it's no longer in the shrinking window.
                if window_counts[nums[start]] == 0:
                    del window_counts[nums[start]]

                # Move the left boundary ('start' pointer) one step to the right, effectively shrinking the window.
                # The loop will then re-check if the *new* window [start...end] is still complete.
                start += 1

        # After iterating through all possible 'end' positions, return the total count found.
        return count
                

if __name__ == "__main__":
    s = Solution()
    # print(s.countCompleteSubarrays([1,3,1,2,2]))  # Output: 4
    print(s.countCompleteSubarrays([5, 5, 5, 5]))     # Output: 10
    print(s.countCompleteSubarrays([1, 2, 3, 4]))     # Output: 1
    print(s.countCompleteSubarrays([1, 2, 3]))         # Output: 1