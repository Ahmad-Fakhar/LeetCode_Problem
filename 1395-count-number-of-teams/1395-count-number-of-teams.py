class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        count = 0
        
        # Iterate through each soldier's rating as the middle soldier
        for j in range(1, n - 1):
            left_less = left_greater = right_less = right_greater = 0
            
            # Count soldiers on the left side of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            # Count soldiers on the right side of j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1
            
            # Calculate the number of valid teams with rating[j] as the middle soldier
            count += left_less * right_greater + left_greater * right_less
        
        return count