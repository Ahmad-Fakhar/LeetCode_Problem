class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
            # Define directions: East (right), South (down), West (left), North (up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize the result list with the start position
        result = [(rStart, cStart)]
        # Set to track visited positions
        visited = set(result)
        
        # Step size and direction index
        steps = 1
        dir_idx = 0
        
        while len(result) < rows * cols:
            for _ in range(2):  # Repeat twice for the current step size (once for the row, once for the column)
                for _ in range(steps):
                    rStart += directions[dir_idx][0]
                    cStart += directions[dir_idx][1]
                    
                    # Check if we are within the grid boundaries
                    if 0 <= rStart < rows and 0 <= cStart < cols and (rStart, cStart) not in visited:
                        result.append((rStart, cStart))
                        visited.add((rStart, cStart))
                        
                # Change direction
                dir_idx = (dir_idx + 1) % 4
            
            # Increase the steps after completing a loop in both directions
            steps += 1
        
        return result
            