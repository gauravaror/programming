# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head.next
        while True:
            if fast == None:
                return slow
            if  fast.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next
