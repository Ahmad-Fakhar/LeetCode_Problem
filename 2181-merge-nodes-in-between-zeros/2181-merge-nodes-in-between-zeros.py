# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode(-1)
        tmp=0
        head=head.next
        pointer=new_head

        while (head!=None):
            if(head.val==0):
                new_node=ListNode(tmp)
                pointer.next=new_node
                pointer=new_node
                
                tmp=0
            else:
                tmp+=head.val
            head=head.next
        return new_head.next