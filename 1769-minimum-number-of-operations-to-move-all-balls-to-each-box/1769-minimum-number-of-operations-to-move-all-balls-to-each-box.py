class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lex=[]
        n=len(boxes)
        for i in range(n):
            if boxes[i] == "1":
                lex.append(i)
        ans=[]
        for i in range(n):
            tem=0
            for j in lex:
                tem=tem + abs(i-j)
            ans.append(tem)
        return ans
