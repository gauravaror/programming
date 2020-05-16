# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = None
        evenhead = None
        nex = head
        i = 1
        while nex:
            if even:
                even.next = nex.next
                even = even.next
                #even.next = None
            else:
                even = nex.next
                evenhead = even
            if nex.next:
                nex.next = nex.next.next
            if nex.next:
                nex = nex.next
            else:
                nex.next = evenhead
                break
        return head
