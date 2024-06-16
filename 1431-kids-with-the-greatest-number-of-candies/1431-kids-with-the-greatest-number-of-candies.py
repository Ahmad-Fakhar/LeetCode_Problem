class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         # Calculate the current maximum number of candies any kid has
        max_candies = max(candies)
        
        # Determine if each kid can have the greatest number of candies after receiving extraCandies
        result = [(candy + extraCandies) >= max_candies for candy in candies]
        
        return result