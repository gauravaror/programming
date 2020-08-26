class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        hh = []
        c = Counter()
        for i in nums:
            c[i] += 1
        for ka,v in c.items():
            heapq.heappush(hh, (ka, v))
        group = 0
        while len(hh) > 0:
            lis = []
            doubles = []
            while len(lis) < k and len(hh) > 0:
                elem, occurance = heapq.heappop(hh)
                if len(lis) > 0:
                    if not (lis[-1] + 1 == elem):
                        return False
                lis.append(elem)
                occurance -= 1
                if occurance > 0:
                    doubles.append((elem, occurance))
            if len(lis) == k:
                group += 1
            print(lis, doubles)
            for ka,v in doubles:
                heapq.heappush(hh, (ka,v))
        
        return  len(nums)//k == group
