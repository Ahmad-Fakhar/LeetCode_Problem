class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
            # Step 1: Find the minimum elements in each row
        min_row_elements = {min(row) for row in matrix}

        # Step 2: Find the maximum elements in each column
        max_col_elements = set()
        for col in range(len(matrix[0])):
            max_col = max(matrix[row][col] for row in range(len(matrix)))
            max_col_elements.add(max_col)

        # Step 3: The intersection of the two sets gives us the lucky numbers
        lucky_numbers = list(min_row_elements & max_col_elements)

        return lucky_numbers