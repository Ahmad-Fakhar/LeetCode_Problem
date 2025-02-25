class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        o, e, s, r = 0, 1, 0, 0
        
        for a in arr:
            s += a
            if s % 2 == 0:
                r = (r + o) % MOD
                e += 1
            else:
                r = (r + e) % MOD
                o += 1
                
        return r
        