# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ho = []
        for idx,i in enumerate(lists):
            #print(i, i.val, idx)
            if i:
                heapq.heappush(ho, (i.val, idx, i))
        head = None
        temp = None
        while (len(ho) > 0):
            #print(ho)
            elem_tup = heapq.heappop(ho)
            elem = elem_tup[2]
            if not head:
                head = copy.deepcopy(elem)
                head.next = None
            elif not head.next:
                head.next = elem
                temp = elem
            else:
                temp.next = elem
                temp = elem
            if elem.next:
                elem = elem.next
                heapq.heappush(ho, (elem.val, elem_tup[1], elem))
        return head
