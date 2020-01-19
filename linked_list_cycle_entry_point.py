# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = {}
        if head == None:
            return None
        index = 0
        while True:
            if head.next == None:
                return None
            if head in nodes:
                return head
            nodes[head] = head
            index += 1
            head = head.next
