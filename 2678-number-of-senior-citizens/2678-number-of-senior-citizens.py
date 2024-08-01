class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in (details):
            age = int(i[11:13])  
            if age > 60:
                res +=1
        return res
