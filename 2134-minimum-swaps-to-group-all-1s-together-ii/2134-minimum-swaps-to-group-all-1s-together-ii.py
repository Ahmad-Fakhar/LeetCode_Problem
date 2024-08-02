class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = sum(nums)
        
        if count_ones == 0 or count_ones == n:
            return 0

        # Extend the array to handle circular nature
        extended_nums = nums + nums[:count_ones - 1]
        
        # Find the max number of 1s in any window of size count_ones
        max_ones_in_window = 0
        current_ones_in_window = 0
        
        # Initial window
        for i in range(count_ones):
            current_ones_in_window += extended_nums[i]
        
        max_ones_in_window = current_ones_in_window
        
        # Slide the window
        for i in range(count_ones, len(extended_nums)):
            current_ones_in_window += extended_nums[i] - extended_nums[i - count_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        # Minimum swaps needed
        return count_ones - max_ones_in_window