class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def operation(arr):
            arr.sort()
            curr = 1
            result = 1

            for i in range(1,len(arr)):
                if arr[i] == arr[i-1]+1:
                    curr+=1
                else:
                    result = max(result,curr)
                    curr = 1
                result = max(result,curr)
            return result+1
        hor = operation(hBars)
        ver = operation(vBars)
        res = min(hor,ver)
        return res*res