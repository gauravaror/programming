# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            head = None
            headst = None
            while l1 and l2:
                if l1.val > l2.val:
                    if head:
                        head.next = l2
                        head = l2
                    else:
                        head = l2
                        headst = l2
                    l2 = l2.next
                else:
                    if head:
                        head.next = l1
                        head = l1
                    else:
                        head = l1
                        headst = l1
                    l1 = l1.next
            if l1:
                head.next = l1
            if l2:
                head.next = l2
            return headst
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
