class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        for i in range(1, 2001):
            if not i in arr:
                missing += 1
                if missing == k:
                    return i
