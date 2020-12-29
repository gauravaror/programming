def make():
    return [None, None]

class Trie:
    def __init__(self):
        self.root = make()
    
    def insert(self, x):
        cur = self.root
        for i in range(30, -1, -1):
            if not cur[x >> i & 1]:
                cur[x >> i & 1] = make()
            cur = cur[x >> i & 1]

    def query(self, x):
        cur = self.root
        ans = 0
        for i in range(30, -1, -1):
            want = (x >> i & 1) ^ 1
            if cur[want] != None:
                ans += 2**i
                cur = cur[want]
            elif cur[want^1] != None:
                cur = cur[want^1]
            else:
                return -1
        return ans
                
                
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        tri = Trie()
        for idx,query in enumerate(queries):
            query.append(idx)
        queries.sort(key=lambda x: x[1])
        answer = [-1]*len(queries)
        i = 0
        for x,m,qid in queries:
            while i < len(nums) and nums[i] <= m:
                tri.insert(nums[i])
                i += 1
            answer[qid] = tri.query(x)
        return answer
