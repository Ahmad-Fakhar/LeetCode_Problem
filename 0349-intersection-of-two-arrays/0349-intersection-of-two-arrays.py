class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return (set(nums1).intersection(set(nums2)))
        return (set(nums1) & (set(nums2)))

        # a =set(nums1)
        # arr =[]
        # for i in nums2 :
        #     if i in a:
        #         arr.append(i)
        #         ans=set(arr)
        # return ans
        

        x = set(nums1)
        returnArray = []

        for i in nums2:
            if i in x:
                returnArray.append(i)
        returnArray = set(returnArray)

        return returnArray