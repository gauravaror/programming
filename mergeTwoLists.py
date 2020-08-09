# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        headst = None
        while l1 and l2:
            if l1.val < l2.val:
                if head == None:
                    head = l1
                    headst = head
                else:
                    head.next = l1
                    head = head.next
                l1 = l1.next
            else:
                if head == None:
                    head = l2
                    headst = head
                else:
                    head.next = l2
                    head = head.next
                l2 = l2.next
                head.next = l2
                
        if l1:
            if head == None:
                headst = l1
            else:
                head.next = l1
        if l2:
            if head == None:
                headst = l2
            else:
                head.next = l2
        return headst
