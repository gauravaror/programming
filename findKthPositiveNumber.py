class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        first = arr[0]
        carr = [arr[i] - i - 1 for i in range(len(arr))]
        biindex = bisect.bisect_left(carr, k)
        if biindex >= len(arr):
            biindex = len(arr)-1
            return arr[biindex] + (k-carr[biindex])
        return arr[biindex] + (k-1-carr[biindex])
