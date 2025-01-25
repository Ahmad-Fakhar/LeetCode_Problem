class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted(nums)
        ht_g = {}
        ht_e = {arr[0]:0}
        g = 0
        s = 0
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] <= limit:
                pass
            else:
                ht_g[g] = arr[s:i][::-1] 
                g += 1
                s = i 
            ht_e[arr[i]] = g
        ht_g[g] = arr[s:][::-1]
        result = []
        for num in nums:
            result.append(ht_g[ht_e[num]].pop())
        return result