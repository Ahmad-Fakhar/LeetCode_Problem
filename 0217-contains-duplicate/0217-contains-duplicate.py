class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = set(nums)
        # if len(n) == len(nums):
        #     return False
        # else:
        #     return True     


        return len(set(nums)) != len(nums)


        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False