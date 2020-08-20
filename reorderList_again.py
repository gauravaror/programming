# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast == slow:
            return head
        print(slow.val)
        if prev:
            prev.next = None
        prev = None
        while slow.next:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        slow.next = prev
        headst = head
        save = None
        while head and slow:
            tmphead, tmpslow = head.next, slow.next
            slow.next = tmphead
            head.next = slow
            save = slow
            slow = tmpslow
            head = tmphead
        if slow and save:
            save.next = slow
        return headst
