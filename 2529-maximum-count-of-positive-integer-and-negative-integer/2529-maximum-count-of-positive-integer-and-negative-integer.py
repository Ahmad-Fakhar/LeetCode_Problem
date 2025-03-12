class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        positive_count = n - left

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
       
        negative_count = right + 1

        return max(positive_count, negative_count)
        