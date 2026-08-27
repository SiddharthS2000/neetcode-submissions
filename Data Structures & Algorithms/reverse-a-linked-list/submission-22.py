# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iterative
        # prev = None
        # curr = head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev


        # stack

        # if not head:
        #     return head
        # stack = []
        # ptr = head
        # while ptr:
        #     stack.append(ptr)
        #     ptr = ptr.next

        # head = stack.pop()
        # ptr = head
        # while ptr and stack:
        #     ptr.next = stack.pop()
        #     ptr = ptr.next

        # ptr.next = None

        # return head


        # recursive
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head