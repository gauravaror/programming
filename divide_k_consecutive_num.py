from typing import List
import math
class Solution:
    def can_insert(self, st: List[int], num: int, k: int) -> bool:
        if len(st) >= k:
            return False
        if num in st:
            return False
        print("Find ", st, abs(st[len(st)-1] - num))
        if abs(st[len(st)-1] - num) < k:
            return True
        for i in st:
            if abs(i-num) == 1:
                return True
        return False
        
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        total_elems = len(nums)
        divisible_by_k = (total_elems % k) == 0
        if not divisible_by_k:
            return False
        num_sets = total_elems/k
        #nums.sort()
        sets = []
        for i in nums:
            inserted = False
            for s in sets:
                if not inserted:
                    print("Can insert", s, self.can_insert(s, i, k), i)
                    if self.can_insert(s, i, k):
                        for pos,item in enumerate(s):
                            if item < i:
                                inserted = True
                                s.insert(pos, i)
                                break
                        if not inserted:
                            s.append(i)
                            inserted = True
                            break
            if not inserted:
                print("Sets", len(sets), num_sets)
                if len(sets) > num_sets:
                    return False
                sets.append([i])
            print(sets)
        for s in sets:
            if not len(s) == k:
                return False
            prev = None
            for item in s:
                if prev == None:
                    prev=item
                else:
                    print("Checking ", prev, item)
                    if not (prev - item) == 1:
                        return False
                    prev = item
                    
        return True
                                
sol = Solution()
assert sol.isPossibleDivide([1,2,3,3,4,4,5,6], 4) == True
assert sol.isPossibleDivide( [3,2,1,2,3,4,3,4,5,9,10,11], 3) == True
assert sol.isPossibleDivide([3,3,2,2,1,1], 3) == True
assert sol.isPossibleDivide([1,2,3,4], 3) == False
assert sol.isPossibleDivide([1,3,4,2,5,6], 3) == True
#print(sol.isPossibleDivide([1,2,3,3,4,4,5,6], 4))
