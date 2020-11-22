from collections import Counter
from typing import List
class SegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0]*(2*self.size)

    def modify(self, index: int, value: int):
        index += self.size
        self.tree[index] = value
        while index > 1:
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1

    def query(self, left: int, right: int):
        left += self.size
        right += self.size
        res = 0
        while left < right:
            if left&1:
                res += self.tree[left]
                left += 1
            if right&1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        #print("ins", instructions)
        c = Counter()
        cost = 0
        len_ins = len(instructions)
        seg = SegmentTree(max(instructions)+1)
        for idx,i in enumerate(instructions):
            less = seg.query(0, i)
            equal = c[i]
            print("Less Equal", less, equal, cost)
            cost += min(less, idx-less-equal)
            seg.modify(i, equal + 1)
            c[i] += 1
        return cost % (10**9 + 7)
if __name__ == '__main__':
    sol = Solution()
    print(sol.createSortedArray([1,2,3,6,5,4]))
    print(sol.createSortedArray([1,3,3,3,2,4,2,1,2]))
    print(sol.createSortedArray([1,5,6,2]))


