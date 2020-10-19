class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check_possible(A, B, num):
            moved = 0
            for a,b in zip(A, B):
                if a != num and b != num:
                    return -1
                if a != num and b == num:
                    moved += 1
            return moved
        possible = -1
        for i in range(1, 7):
            m = check_possible(A, B, i)
            #print(i, m)
            if m != -1:
                if possible == -1:
                    possible = m
                possible = min(possible, m)
            m = check_possible(B, A, i)
            #print(i, m)
            if m != -1:
                if possible == -1:
                    possible = m
                possible = min(possible, m)
        return possible
