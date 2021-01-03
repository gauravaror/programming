class Solution:
    def countArrangement(self, n: int) -> int:
        print("elements", n)
        def beautiful(elements):
            for idx, elem in enumerate(elements, 1):
                if idx % elem != 0 or elem % idx != 0:
                    return False
            return True
        self.ans = 0
        def backtrack(current, elements):
            if len(current) == n:
                self.ans += 1
                return
            for idx in range(len(elements)):
                current_idx = len(current) + 1
                if elements[idx] % current_idx == 0 or current_idx % elements[idx] == 0:
                    backtrack(current+[elements[idx]], elements[:idx] + elements[idx+1:])
        backtrack([], list(range(1,n+1)))
        return self.ans
