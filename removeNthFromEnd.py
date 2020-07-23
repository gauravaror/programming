# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        copy = head
        nodes = 0
        while copy:
            nodes += 1
            copy = copy.next
        nodes -= n
        copy = head
        nn = 0
        while nn < nodes-1:
            nn += 1
            copy = copy.next
        if nodes == 0:
            return head.next
        copy.next = copy.next.next
        return head
