# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
            # Initialize pointers
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        next = curr.next

        # List to store the positions of critical points
        critical_positions = []
        index = 1

        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                critical_positions.append(index)
            prev = curr
            curr = next
            next = next.next
            index += 1

        # If there are fewer than two critical points, return [-1, -1]
        if len(critical_positions) < 2:
            return [-1, -1]

        # Calculate minimum and maximum distances between critical points
        min_distance = float('inf')
        max_distance = critical_positions[-1] - critical_positions[0]

        for i in range(1, len(critical_positions)):
            min_distance = min(min_distance, critical_positions[i] - critical_positions[i - 1])

        return [min_distance, max_distance]
