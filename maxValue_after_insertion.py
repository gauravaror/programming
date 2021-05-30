class Solution:
    def maxValue(self, n: str, x: int) -> str:
        start = 0
        end = len(n)
        if n[0] == '-':
            start = 1
        max_ = -float('inf')
        contributions = [0]*len(n)
        right = [0]*len(n)
        lena = end-start - 1
        for i in range(start, end):
            contributions[i] = int(n[i]) * (10**lena)
            lena -= 1
        for i in range(start, end):
            right[i] = contributions[i]
            if i > 0:
                right[i] += right[i-1]
        total = right[-1]
        max_ = -float('inf')
        for i in range(start, end+1):
            left = 0 if i == 0 else right[i-1]
            all_sum = left*10 + (total - left) + x*(10**(end-i))
            final_sum = all_sum if start == 0 else -all_sum
            max_ = max(max_, final_sum)
        return str(max_)
        
