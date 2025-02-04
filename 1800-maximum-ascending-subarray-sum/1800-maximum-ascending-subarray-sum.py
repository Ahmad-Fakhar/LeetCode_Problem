class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curent = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] > nums[i-1]:
                curent += nums[i]
            else:
                max_sum = max(curent,max_sum)
                curent = nums[i]
        return max(curent,max_sum)
        