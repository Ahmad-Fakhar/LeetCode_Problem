class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
                # Initialize the minimum and maximum values from the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # Initialize the maximum distance found so far
        max_dist = 0
        
        # Iterate through the rest of the arrays
        for i in range(1, len(arrays)):
            # Calculate the potential max distance with the current array's min and max
            max_dist = max(max_dist, abs(arrays[i][-1] - min_val), abs(arrays[i][0] - max_val))
            
            # Update the global minimum and maximum values
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_dist