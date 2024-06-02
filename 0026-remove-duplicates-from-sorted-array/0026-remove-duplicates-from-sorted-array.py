class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]
        return l + 1

        