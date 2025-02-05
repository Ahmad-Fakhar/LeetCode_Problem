class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if s1 == s2:
            return True

        diffs = 0
        firstIdx = -1
        secondIdx = -1

        for i in range(n):
            if s1[i] != s2[i]:
                diffs += 1

                if diffs > 2:
                    return False
                elif diffs == 1:
                    firstIdx = i
                else:
                    secondIdx = i

        return diffs == 2 and s1[firstIdx] == s2[secondIdx] and s1[secondIdx] == s2[firstIdx]


        