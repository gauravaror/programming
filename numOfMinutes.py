class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree_heir = collections.defaultdict(list)
        for idx,i in enumerate(manager):
            tree_heir[i].append(idx)
        rcost = -float('inf')
        stack = [(headID, 0)]
        while len(stack) > 0:
            emp, cost = stack.pop()
            rcost = max(rcost, cost)
            cost += informTime[emp]
            for sub in tree_heir[emp]:
                stack.append((sub, cost))
        return rcost
