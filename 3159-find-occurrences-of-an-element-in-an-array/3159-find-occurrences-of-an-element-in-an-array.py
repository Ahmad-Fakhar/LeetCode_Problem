class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            if  x == nums[i]:
                indices.append(i)
        res = []
        for i in range(len(queries)):
            if queries[i]<=len(indices):
                res.append(indices[queries[i]-1])
            else:
                res.append(-1)
        return res