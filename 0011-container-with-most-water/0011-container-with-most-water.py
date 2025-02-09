class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,res,r=0,0,len(height)-1

        while l<r:
            w = r-l
            H=min(height[l],height[r])
            area = H*w
            res=max(area,res)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res


        # left = 0
        # right = len(height) - 1
        # result = 0

        # while left < right:

        #     h = min(height[left], height[right])
            
        #     w = right - left
        #     area = w * h
        #     result = max(result, area)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
                
        # return result