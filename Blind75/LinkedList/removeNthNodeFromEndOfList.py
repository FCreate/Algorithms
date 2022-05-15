#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = it1 = it2 = head
        i = 0
        while i < n:
            i += 1
            it1 = it1.next
        if it1:
            while it1.next:
                it1 = it1.next
                it2 = it2.next
            it2.next = it2.next.next
        else:
            res = res.next
        return res