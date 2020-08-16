class Solution:
    def minOperations(self, n: int) -> int:
        start = 0
        end = n-1
        total_opps = 0
        while start < end:
            first = 2*start + 1
            second = 2*end + 1
            ops_needed = (second-first)//2
            total_opps += ops_needed
            start += 1
            end -= 1
        return total_opps
