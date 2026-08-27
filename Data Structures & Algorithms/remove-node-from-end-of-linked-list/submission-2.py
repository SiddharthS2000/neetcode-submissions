# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []

        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next

        remove_index = len(node_list) - n
        if remove_index == 0:
            return head.next
        
        node_list[remove_index - 1].next = node_list[remove_index].next
        return head
            