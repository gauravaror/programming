class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(index, current, sum_):
            if index >= len(candidates):
                return
            if sum_  == target:
                output.append(current)
                return
            if sum_ > target:
                return
            backtrack(index, current + [candidates[index]], sum_ + candidates[index])
            #backtrack(index+1, current + [candidates[index]], sum_ + candidates[index])
            backtrack(index+1, current, sum_)
        backtrack(0, [],  0)
        return output 
