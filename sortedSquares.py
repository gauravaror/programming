class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        hh = []
        output = []
        for i in range(len(nums)):
            if nums[i] < 0:
                heapq.heappush(hh, abs(nums[i]))
            else:
                while hh and hh[0] <= nums[i]:
                    elem =  heapq.heappop(hh)
                    output.append(elem**2)
                output.append(nums[i]**2)
        while len(hh) > 0:
            elem = heapq.heappop(hh)
            output.append(elem**2)
        return output
