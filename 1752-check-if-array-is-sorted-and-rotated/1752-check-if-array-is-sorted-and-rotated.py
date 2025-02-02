class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        num = len(nums)

        for i in range(num):
            if nums[i] > nums[(i + 1) % num]: 
                count += 1

        return count <= 1 
        