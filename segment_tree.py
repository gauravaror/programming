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
if __name__ == '__main__':
    lis = [2,3,1,1,1,1,1,1,1]
    seg = SegmentTree(len(lis))
    for i in range(len(lis)):
        seg.modify(i, lis[i])
        print(i, seg.query(0, i))
                

