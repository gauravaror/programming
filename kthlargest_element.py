import heapq as pq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            pq.heappush(h, i)
            while len(h) > k:
                pq.heappop(h)
        return h[0]
