# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_list_current = dummy
        
        # Initialize the current pointer and the sum accumulator
        current = head.next  # Start from the node after the initial 0
        sum_accumulator = 0
        
        while current is not None:
            if current.val == 0:
                # If current node is zero and sum_accumulator is not zero,
                # create a new node with the accumulated sum and add it to the new list
                if sum_accumulator != 0:
                    new_node = ListNode(sum_accumulator)
                    new_list_current.next = new_node
                    new_list_current = new_node
                    sum_accumulator = 0
            else:
                # Accumulate the values between zeros
                sum_accumulator += current.val
            
            current = current.next
        
        return dummy.next

    # Helper function to create a linked list from a list of values
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to print the linked list
    def print_linked_list(head):
        current = head
        while current is not None:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print()