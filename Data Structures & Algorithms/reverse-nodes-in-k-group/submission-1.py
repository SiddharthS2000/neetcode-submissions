# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of a linked list in groups of size k.
        If fewer than k nodes remain, leave them unchanged.
        """
        # Dummy node before head simplifies edge cases
        dummy = ListNode(0, head)
        prevGroupTail = dummy

        while True:
            # Find the kth node ahead of prevGroupTail
            kthNode = self.getKthNode(prevGroupTail, k)
            if not kthNode:
                break  # Not enough nodes left to reverse

            nextGroupHead = kthNode.next  # Node after the current group

            # Reverse the current group
            prev, curr = nextGroupHead, prevGroupTail.next
            while curr != nextGroupHead:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            # Reconnect reversed group with previous part of the list
            oldGroupHead = prevGroupTail.next
            prevGroupTail.next = kthNode
            prevGroupTail = oldGroupHead  # Move tail pointer to end of reversed group

        return dummy.next

    def getKthNode(self, start: ListNode, k: int) -> Optional[ListNode]:
        """
        Return the kth node from 'start', or None if fewer than k remain.
        """
        while start and k > 0:
            start = start.next
            k -= 1
        return start
