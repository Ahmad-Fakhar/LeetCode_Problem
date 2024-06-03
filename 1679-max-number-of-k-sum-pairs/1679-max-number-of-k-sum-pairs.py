class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans = 0
        nums.sort()
        lf,rt = 0, len(nums)-1
        
        while lf<rt:
            
            if nums[lf] + nums[rt] > k:
                rt -=1
            elif nums[lf] + nums[rt] < k:
                lf+=1
            else:
                ans+=1
                lf +=1
                rt -= 1
        return ans 