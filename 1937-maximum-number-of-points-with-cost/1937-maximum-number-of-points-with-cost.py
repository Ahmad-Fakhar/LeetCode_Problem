class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        dp = points[0][:]  # Start with the first row

        for r in range(1, m):
            left_to_right = [0] * n
            right_to_left = [0] * n
            
            # Calculate left-to-right max array
            left_to_right[0] = dp[0]
            for c in range(1, n):
                left_to_right[c] = max(left_to_right[c-1] - 1, dp[c])
            
            # Calculate right-to-left max array
            right_to_left[-1] = dp[-1]
            for c in range(n-2, -1, -1):
                right_to_left[c] = max(right_to_left[c+1] - 1, dp[c])
            
            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left_to_right[c], right_to_left[c])
        
        return max(dp)