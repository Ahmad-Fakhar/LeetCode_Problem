class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Sort the nums based on frequency and then by value
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums