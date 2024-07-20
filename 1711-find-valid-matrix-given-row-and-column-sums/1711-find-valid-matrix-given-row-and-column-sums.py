class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        

        m, n = len(rowSum), len(colSum)

        arr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                arr [i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= arr[i][j]
                colSum[j] -= arr[i][j]
        return arr