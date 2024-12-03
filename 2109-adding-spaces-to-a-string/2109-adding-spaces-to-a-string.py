class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        l = 0
        for i in spaces:
            ans += s[l:i] + " " 
            l = i

        ans += s[i:]
        return ans