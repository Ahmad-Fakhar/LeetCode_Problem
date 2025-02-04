# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head
        odd = head
        even = head.next
        evenhead = even  # Save the start of even nodes
        
        while even and even.next:
            odd.next = even.next  # Connect odd nodes
            odd = odd.next  # Move odd pointer
            
            even.next = odd.next  # Connect even nodes
            even = even.next  # Move even pointer
        
        odd.next = evenhead  # Connect last odd node to the first even node
        return head

        