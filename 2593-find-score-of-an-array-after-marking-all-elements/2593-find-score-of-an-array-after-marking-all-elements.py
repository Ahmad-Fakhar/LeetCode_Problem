class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0  # Initialize score to 0
        marked = [False] * n  # Create a list to track which elements are marked
        
        while not all(marked):  # Repeat until all elements are marked
            min_value = float('inf')
            min_index = -1
            for i in range(n):
                if not marked[i] and nums[i] < min_value:
                    min_value = nums[i]
                    min_index = i
            score += nums[min_index]           
            # Mark the chosen element and its adjacent elements
            marked[min_index] = True
            if min_index - 1 >= 0:
                marked[min_index - 1] = True
            if min_index + 1 < n:
                marked[min_index + 1] = True
        
        return score  
            

        