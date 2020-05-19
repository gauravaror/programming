# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        start = 0
        end = mountain_arr.length()-1
        while start < end:
            mid = (start + end)//2
            print(start, end, mid)
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                if mid == start:
                    break
                end = mid
            else:
                start = mid + 1
        def nbs(s, e, di):
            while s < e:
                mid = (s+e)//2
                print("ds",s,e,mid, di)
                item = mountain_arr.get(mid)
                if item == target:
                    return mid,target
                elif item > target:
                    if di:
                        e = mid - 1
                    else:
                        s = mid + 1
                else:
                    if di:
                        s = mid + 1
                    else:
                        e = mid -1
            return s,mountain_arr.get(s)
        i,v = nbs(0, start, True)
        if v == target:
            return i
        i,v = nbs(start,mountain_arr.length()-1, False)
        if v == target:
            return i
        return -1
