class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = len(nums)
        count = 0      
        for i in range(num) :
            for j in range (i+1,num):
                if nums[i] == nums[j]:
                    count += 1
        return count