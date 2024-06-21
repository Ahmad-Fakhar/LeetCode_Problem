class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        
        # Step 2: Calculate the additional satisfied customers if we use the technique for the first `minutes` minutes
        additional_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        
        # Step 3: Use a sliding window to find the best interval for the technique
        max_additional_satisfied = additional_satisfied
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        # Step 4: Combine the base satisfied customers with the maximum additional customers
        return base_satisfied + max_additional_satisfied
        