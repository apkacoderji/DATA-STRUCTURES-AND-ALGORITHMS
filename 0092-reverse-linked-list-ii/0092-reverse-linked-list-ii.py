# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        
        
        last = head
        pos = 1
        before = 0

        while pos < left:
            before = last
            last = last.next
            pos += 1

        curr = last
        prev = None 
        times = right-left+1

        for _ in range(times):
            curr.next, prev, curr = prev, curr, curr.next
        
        last.next = curr
        if before:
            before.next = prev
            return head


        return prev


        