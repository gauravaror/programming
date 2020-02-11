class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        for i in range(arr_len-1):
            for j in range(i+1, arr_len):
                if arr[i] == 2*arr[j] or 2*arr[i] == arr[j]:
                    return True
        return False
