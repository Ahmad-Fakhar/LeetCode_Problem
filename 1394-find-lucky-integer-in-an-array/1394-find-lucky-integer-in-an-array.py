class Solution:
    def findLucky(self, arr: List[int]) -> int:
        run = [-1]
        Set = set(arr)
        for i in Set:
            if arr.count(i) == i:
                run.append(i)
        return max(run)


        