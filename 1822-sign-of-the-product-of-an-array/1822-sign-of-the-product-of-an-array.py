class Solution:
    def arraySign(self, nums):
        product = 1
        for i in nums:
            product *= i 
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else: 
            return 0 




        # for num in nums:
        #     if num == 0:
        #         return 0
        #     if num < 0 and num % 2 == 0:
        #         return 1
        #     if 
        # return -1
                
                  
