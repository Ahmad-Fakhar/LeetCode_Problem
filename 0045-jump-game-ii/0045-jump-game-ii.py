class Solution(object):
    def jump(self, nums):
        l, r =0,0
        res = 0
        while  r < (len(nums)-1) :
            maxJ = 0
            for i in range (l,r+1):
                maxJ = max(maxJ,i+nums[i])
            l=r+1
            r=maxJ
            res+=1 
        return res