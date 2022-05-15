#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        fast, slow = head, head
        while fast and slow and fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False