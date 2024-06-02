class Solution:
    def maxArea(self, height):
        lp = 0
        rp = len(height) - 1
        res = 0
        while lp < rp:
            w = rp - lp
            h = min(height[lp], height[rp])
            a = w * h
            res = max(res, a)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return res
