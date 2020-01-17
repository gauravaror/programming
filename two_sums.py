class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unums = [(i,idx) for idx,i in enumerate(nums)]
        unums = sorted(unums, key=lambda x: x[0])
        start = 0
        end = len(unums) - 1
        while (start< end):
            csum = unums[start][0]  + unums[end][0]
            if csum == target:
                return [unums[start][1], unums[end][1]]
            elif csum > target:
                end -= 1
            else:
                start += 1
        return []
