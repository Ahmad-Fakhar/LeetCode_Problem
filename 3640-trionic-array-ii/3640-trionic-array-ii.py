class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEGATIVE_INF = float('-inf')
        s0 = nums[0]
        s1 = NEGATIVE_INF
        s2 = NEGATIVE_INF
        s3 = NEGATIVE_INF
        
        max_trionic_sum = NEGATIVE_INF
        
        for i in range(1, len(nums)):
            val = nums[i]
            prev_val = nums[i-1]
            
            next_s0 = val
            next_s1 = NEGATIVE_INF
            next_s2 = NEGATIVE_INF
            next_s3 = NEGATIVE_INF
            
            if val > prev_val:
                next_s0 = max(val, s0 + val)
                next_s1 = max(s0, s1) + val
                next_s3 = max(s2, s3) + val
            elif val < prev_val:
                next_s2 = max(s1, s2) + val
            
            s0, s1, s2, s3 = next_s0, next_s1, next_s2, next_s3
            
            if s3 > max_trionic_sum:
                max_trionic_sum = s3
                
        return int(max_trionic_sum)