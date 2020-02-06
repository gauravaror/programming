class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def get_valid_neig(index):
            doing_pos = True
            doing_neg = True
            for i in range(1, d+1):
                if doing_pos and index + i < len(arr):
                    if arr[index+i]< arr[index]:
                        yield index + i
                    else:
                        doing_pos = False
                if doing_neg and index - i >= 0:
                    if arr[index-i] < arr[index]:
                        yield index - i
                    else:
                        doing_neg = False
        
        dp = [-1]*len(arr)
        
        def get_max_jump():
        for i in range(len(arr)):
            get_max_jump(i)
