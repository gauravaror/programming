from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.csnap = 0
        self.array = defaultdict(list)
        for i in range(length):
            self.array[i].append((self.csnap,0))
        

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.csnap, val))
        

    def snap(self) -> int:
        rsnap = self.csnap
        self.csnap += 1
        return rsnap
        

    def get(self, index: int, snap_id: int) -> int:
        bsarray = self.array[index]
        start = 0
        end = len(bsarray)
        while start < end:
            mid = start + (end-start)//2
            if bsarray[mid][0] > snap_id:
                end = mid
            else:
                start = mid + 1
        #print(bsarray, start)
        return bsarray[start-1][1]    
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
