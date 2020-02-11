class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hs = {}
        for i in arr:
            if (i*2) in hs or (i/2) in hs:
                return True
            hs[i] = True
        return False
