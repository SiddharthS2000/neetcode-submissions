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

        if not head or not head.next:
            return head
        # stack
        stk = []
        ptr = head 
        while ptr.next != None: 
            stk.append(ptr) 
            ptr = ptr.next
    
        # Pop from stack and replace 
        # current nodes value' 
        head = ptr 
        while len(stk) != 0: 
            ptr.next = stk.pop() 
            ptr = ptr.next
        
        ptr.next = None
        return head