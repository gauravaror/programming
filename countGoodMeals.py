class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        tp = [pow(2,i) for i in range(42)]
        hmap = Counter()
        ans = 0
        for i in deliciousness:
            for t in tp:
                if t-i in hmap:
                    ans += hmap[t-i]
            hmap[i] += 1
        return int(ans % (pow(10,9) + 7))
                    
        
        
