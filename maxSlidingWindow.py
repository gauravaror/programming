from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k):
            heappush(window, (-1*nums[i], i))
        output = []
        #print(window, window[0])
        output.append(-1*window[0][0])
        current = k
        invalid_idx = []
        while current < len(nums):
            invalid_idx.append(current-k)
            heappush(window, (-1*nums[current], current))
            top_elem = window[0]
            while top_elem[1] in invalid_idx:
                invalid_idx.remove(top_elem[1])
                heappop(window)
                top_elem = window[0]
            #print(window, invalid_idx, current, k)
            output.append(-1*window[0][0])
            current += 1
        return output
