class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(len(nums)):
                    for l in range(k + 1, len(nums)):
                        if k != i and k !=j and l != i and l !=j:
                            p1 = nums[i]*nums[j]
                            p2 = nums[k]*nums[l]
                            if p1==p2:
                                res +=1
                
                        
        return res*4
        