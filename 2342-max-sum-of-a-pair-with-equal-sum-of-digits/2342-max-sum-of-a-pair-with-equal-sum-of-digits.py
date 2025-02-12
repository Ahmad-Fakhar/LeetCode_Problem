class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        
        def digit_sum(n: int) -> int:
            return sum(int(d) for d in str(n))  
        
        sum_dict = {}  
        max_sum = -1

        for num in nums:
            dsum = digit_sum(num)
            if dsum in sum_dict:
                max_sum = max(max_sum, num + sum_dict[dsum])
                sum_dict[dsum] = max(sum_dict[dsum], num) 
            else:
                sum_dict[dsum] = num 

        return max_sum

        