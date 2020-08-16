class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr[0] = 1 if arr[0] % 2 != 0 else 0
        more_than = False
        for i in range(1, len(arr)):
            if arr[i] % 2 != 0:
                arr[i] = arr[i-1] + 1
            else:
                arr[i] = 0
            if arr[i] >= 3:
                more_than = True
        return more_than
