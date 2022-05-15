#https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda x, y: x.val < y.val
        q = PriorityQueue()
        start = curr = ListNode()
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            curr.next = q.get()[1]
            curr = curr.next

            if curr.next:
                q.put((curr.next.val, curr.next))
        return start.next
