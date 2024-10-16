class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # arr = [0] + flowerbed + [0]

        # for i in range(1, len(arr) - 1):
        #     if arr[i] == 0 and arr[i - 1] == 0 and arr[i + 1] == 0:
        #         arr[i] = 1
        #         n -= 1
        #         if n <= 0:
        #             return True
        
        # return n <= 0
        for i in range (len(flowerbed)-1):
             if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i]=1
                n-=1
                if n<=0:
                    return True
        return n <= 0