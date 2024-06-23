class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # creat min and max heap 
        min_heap = []
        max_heap = []
        
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            # Add the current number to both heaps
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))
            
            # While the window is invalid, move the left pointer to the right
            while -max_heap[0][0] - min_heap[0][0] > limit:
                left += 1
                # Remove elements not within the window from the heaps
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
            
            # Calculate the maximum length of the valid window
            ans = max(ans, right - left + 1)
        
        return ans