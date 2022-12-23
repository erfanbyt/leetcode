# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if not cur.next:
            return cur
        if not cur.next.next:
            return cur.next

        faster_cur = head.next.next


        while faster_cur and faster_cur.next:
            cur = cur.next
            faster_cur = faster_cur.next.next

        return cur.next
