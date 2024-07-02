class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(arr, x, start):

            low, high = start, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid
            return -1

    # Sort both arrays
        nums1.sort()
        nums2.sort()
        
        # Choose the smaller array to iterate over
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        result = []
        start = 0
        
        for num in nums1:
            idx = binary_search(nums2, num, start)
            if idx != -1:
                result.append(num)
                start = idx + 1  # Move start to the next element to handle duplicates
                
        return result

