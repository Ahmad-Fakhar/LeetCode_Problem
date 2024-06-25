# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        # delt from start
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        
        #delt from the rest
        temp = head
        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head