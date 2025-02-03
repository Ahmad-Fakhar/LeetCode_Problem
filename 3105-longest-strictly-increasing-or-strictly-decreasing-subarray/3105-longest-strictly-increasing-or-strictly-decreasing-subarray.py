class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        max_length = 1  
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1  
                
            max_length = max(max_length, inc, dec)
        
        return max_length