# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #For if link list is empty or Only one element in that then return head only
        if head == None or head.next == None: 
            return head 
        prev = None
        cur  = head

        while cur != None :
            Nextt = cur.next  # Next value store in Nextt Variable That cosider 2
            cur.next = prev   # update the cur that value already store in prev
            prev = cur        # prev store currently value in head/cur 
            cur = Nextt      # Those Nextt Value store from curr.next assign as currently value 
        return prev