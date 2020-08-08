class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        req_moves = {}
        max_key = 0
        for i,j in zip(s, t):
            d = ord(j) - ord(i)
            if d < 0:
                m = 26+d
            else:
                m = d
            if m == 0:
                continue
            om = m
            while m in req_moves:
                m = req_moves[m]
                m += 26
                if m > k:
                    return False
            if m > max_key:
                max_key = m
            req_moves[m] = m
            req_moves[om] = m
        #print(s, t, req_moves)
        if len(req_moves) == 0:
            return True
        return False if max_key > k  else True
