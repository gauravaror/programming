# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = None
        while True:
            tmp_next = head.next 
            head.next = prev
            if not tmp_next:
                break
            prev = head
            head = tmp_next
        return head
