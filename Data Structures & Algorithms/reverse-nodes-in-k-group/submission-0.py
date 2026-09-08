# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of a linked list in groups of size k.
        If the number of nodes is not a multiple of k, 
        the remaining nodes at the end are left as-is.

        Args:
            head (ListNode): Head of the linked list.
            k (int): Group size for reversal.

        Returns:
            ListNode: New head of the modified linked list.
        """
        # Dummy node simplifies edge cases (e.g., reversing from head)
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node from groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # Not enough nodes left to form a group

            groupNext = kth.next  # Node after the kth (start of next group)

            # Reverse the current group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect previous group to the newly reversed group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp  # Move groupPrev to end of the reversed group

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        """
        Return the kth node from the current node, or None if fewer than k remain.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
