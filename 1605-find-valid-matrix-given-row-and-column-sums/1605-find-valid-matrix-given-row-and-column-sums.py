class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        # Initialize the result matrix with zeros
        result = [[0] * n for _ in range(m)]
        
        i = 0
        j = 0
        # Iterate until we fill all the rows and columns as per their sums
        while i < m and j < n:
            # Assign the minimum of the current row sum and column sum to the matrix cell
            min_value = min(rowSum[i], colSum[j])
            result[i][j] = min_value
            # Subtract the assigned value from the respective row and column sums
            rowSum[i] -= min_value
            colSum[j] -= min_value
            # Move to the next row if the current row sum becomes zero
            if rowSum[i] == 0:
                i += 1
            # Move to the next column if the current column sum becomes zero
            if colSum[j] == 0:
                j += 1
        
        return result
        