class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            start = 0
            count = 0
            result = 0
            for end in range(len(nums)):
                if nums[end] % 2 == 1:
                    count += 1
                while count > k:
                    if nums[start] % 2 == 1:
                        count -= 1
                    start += 1
                result += end - start + 1
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)