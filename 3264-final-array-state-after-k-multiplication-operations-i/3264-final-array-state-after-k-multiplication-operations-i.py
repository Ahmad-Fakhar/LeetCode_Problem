class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        multi = multiplier
        num = nums
        for i in range(k):
            a = min(num)
            b = a*multi
            c = num.index(a)
            num[c] = b
            
        return num


        