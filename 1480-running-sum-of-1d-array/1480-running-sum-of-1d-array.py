class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        add = 0
        arr = []
        for i in range(len(nums)):
            add = add + nums[i]
            arr.append(add)
        return arr    

        