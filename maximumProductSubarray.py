class Solution:
    
    def cross_prod(self, left, mid, right):
        lprod_max = self.nums[mid]
        rprod_max = self.nums[mid+1]
        lprod_min = self.nums[mid]
        rprod_min = self.nums[mid+1]
        prev = 1
        for i in range(mid, left-1, -1):
            prev = prev*self.nums[i]
            lprod_max = max(prev, lprod_max)
            lprod_min = min(prev, lprod_min)
        prev = 1
        for j in range(mid+1, right+1, 1):
            prev = prev*self.nums[j]
            rprod_max = max(prev, rprod_max)
            rprod_min = min(prev, rprod_min)
        print("cross sum", left, mid, right, lprod_max, lprod_min, rprod_max, rprod_min)
        return max(rprod_max*lprod_max, lprod_min*rprod_min, rprod_max,lprod_max)


    def helper(self, left , right):
        if left >= right:
            return self.nums[left]
        mid = left +  (right - left)//2
        larray = self.helper(left, mid)
        rarray = self.helper(mid+1, right)
        marray = self.cross_prod(left, mid, right)
        print(left, right, larray, rarray, marray)
        return max(larray, rarray, marray)
    
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        return self.helper(0, len(nums)-1)
