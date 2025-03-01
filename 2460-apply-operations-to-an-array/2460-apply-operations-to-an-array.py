class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = nums[i]*0
        res = [] 
        for i in nums:
            if i != 0:
                res.append(i)
        res += [0] * (n - len(res))
        return res 

        