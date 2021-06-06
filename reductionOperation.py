class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = defaultdict(int)
        for i in nums:
            c[i] += 1
        c= list(c.items())
        d = []
        for i in c:
            d.append(list(i))
        c = d
        c = sorted(c, key=lambda x: x[0])
        index = len(c) - 1
        operations = 0
        while index > 0:
            operations += c[index][1]
            c[index-1][1] += c[index][1]
            index -= 1
        return operations
            
