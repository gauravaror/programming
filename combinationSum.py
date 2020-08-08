class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = {}
        def hash(li):
            return ' '.join([str(l) for l in li])
        def back(candidates, target, solution):
            if target == 0:
                s = sorted(solution)
                answer[hash(s)] = s
            for cand in candidates:
                if target - cand  >= 0:
                    sol = solution.copy()
                    sol.append(cand)
                    back(candidates, target-cand, sol)
        back(candidates, target, [])
        return list(answer.values())
