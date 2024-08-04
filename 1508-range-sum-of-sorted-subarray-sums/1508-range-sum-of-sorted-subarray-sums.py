class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7

        # Step 1: Generate all subarray sums
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Step 2: Sort the subarray sums
        subarray_sums.sort()
        
        # Step 3: Sum the range from left to right (1-indexed, convert to 0-indexed)
        range_sum = sum(subarray_sums[left-1:right]) % MOD
        
        return range_sum