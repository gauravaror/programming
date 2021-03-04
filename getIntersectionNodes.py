class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def listify(head):
            l = []
            while head:
                l.append(head)
                head = head.next
            return l
        A = listify(headA)
        B = listify(headB)
        a = len(A) - 1
        b = len(B) - 1
        while a >=0  and b >= 0 and A[a] == B[b]:
            a -= 1
            b -= 1
        
        if a + 1 < len(A) and b + 1 < len(B) and A[a+1] == B[b+1]:
            return A[a + 1]
        else:
            return None
