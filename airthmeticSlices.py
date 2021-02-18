class Solution(object):
    def numberOfArithmeticSlices(self, A):
        start = 0
        end = 1
        nums = 0
        while end < len(A):
            ediff = A[end] - A[end-1]
            sdiff = A[start+1] - A[start]
            if ediff != sdiff:
                start =  end - 1
                end = start
            elif end - start >= 2:
                nums += (end-start-1)
            end =  end + 1
        return nums
