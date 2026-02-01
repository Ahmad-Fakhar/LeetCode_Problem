class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums.pop(0)
        nums.sort()
        ans += nums[0] + nums[1]
        return ans