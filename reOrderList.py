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
        fp = head
        headcopy = head
        sp = head
        while fp:
            #print(fp.val, sp.val)
            if fp.next:
                fp = fp.next.next
                sp = sp.next
            else:
                fp = fp.next
        # Reverse from slow pointer
        #print(sp.val)
        #return sp
        prev = None
        while sp:
            #print(sp.val)
            save = sp.next
            sp.next = prev
            prev = sp
            #print(save, sp.val)
            if save:
                sp = save
            else:
                break
        #sp = prev
        #print(sp.val, sp.next.val, sp.next.next)
        while headcopy and sp:
            save = headcopy.next
            headcopy.next = sp
            spsave = sp.next
            sp.next = save
            headcopy = save
            sp = spsave
        if headcopy:
            headcopy.next = None
        #print("jjhgg ",headcopy, sp)
        return head
