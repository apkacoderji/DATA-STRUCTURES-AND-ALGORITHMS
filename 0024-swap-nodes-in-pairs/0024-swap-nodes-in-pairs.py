# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        def reverse(left, times):
            curr = left.next
            prev = left
            for _ in range(times):
                curr.next, prev, curr = prev, curr, curr.next
            left.next = curr
                
        
        res = None
        left = head
        prev_left = None

        while True:
            right = left
            for _ in range(2-1):
                if not right:
                    return res
                right = right.next

            if right:
                next_left = right.next
                reverse(left,1)

                if prev_left:
                    prev_left.next = right
                prev_left = left
                left = next_left
                if not res:
                    res = right
            
            else:
                if prev_left:
                    prev_left.next = left
                if not res:
                    res = head
            
        
                return res


        