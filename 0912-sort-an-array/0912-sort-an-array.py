class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(nums, n, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # left = 2*i + 1
            right = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is greater than root
            if left < n and nums[i] < nums[left]:
                largest = left

            # See if right child of root exists and is greater than root
            if right < n and nums[largest] < nums[right]:
                largest = right

            # Change root, if needed
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]  # swap

                # Heapify the root.
                heapify(nums, n, largest)

        def build_max_heap(nums):
            n = len(nums)
            # Build a maxheap.
            for i in range(n // 2 - 1, -1, -1):
                heapify(nums, n, i)

        def heapsort_helper(nums):
            n = len(nums)
            build_max_heap(nums)
            # One by one extract elements
            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]  # swap
                heapify(nums, i, 0)

        heapsort_helper(nums)
        return nums