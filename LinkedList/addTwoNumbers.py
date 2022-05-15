#https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(0)
        mantissa = 0
        while l1 and l2:
            l1_number = l1.val
            l2_number = l2.val
            mantissa, val = divmod(l1_number + l2_number + mantissa, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            l1_number = l1.val
            mantissa, val = divmod(l1_number + mantissa, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        while l2:
            l2_number = l2.val
            mantissa, val = divmod(l2_number + mantissa, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        if mantissa:
            curr.next = ListNode(mantissa)
        return res.next
