class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False  
         
        # count = 0 
        # for i in arr:
        #     if [i] % 2 != 0 and [i+1] % 2 != 0 and [i + 2] % !=0 :
        #         count += 1
        # return count == 1
