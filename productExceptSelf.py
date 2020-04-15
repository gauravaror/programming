class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        front = {0:1}
        back = {len(nums)+1:1}
        for idx,i in enumerate(nums):
            prod = prod*i
            front[idx+1] = prod
        prod = 1
        for idx,i in enumerate(nums[::-1]):
            prod = prod*i
            back[len(nums)-idx] = prod
        output = []
        for idx in range(len(nums)):
            output.append(front[idx]*back[idx+2])
        return output
