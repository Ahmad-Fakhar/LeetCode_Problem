class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        res = left = right = 0

        while  right < (len(nums)-1) :
            maxJump = 0

            for i in range (left, right+1):
                maxJump = max(maxJump, i+nums[i])
            left = right+1
            right = maxJump
            res+=1 

        return res