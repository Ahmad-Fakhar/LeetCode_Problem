class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        count = 0
        if len(words) == len (s):
            for i in range(len(s)):
                if words[i].startswith(s[i]):
                    count +=1
            if count == len(words):
                return True