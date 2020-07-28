# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val = 0
        while head:
            #print(val)
            val = val << 1
            val += head.val
            head = head.next
        return val
