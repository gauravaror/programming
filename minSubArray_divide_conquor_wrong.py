class Solution:
    
    def cross_check(self, left, right, mid):
        left_point = mid
        right_point = mid + 1
        current_sum = 0
        while left_point >= left and right_point <= right:
            reminder = (self.nums_sum - current_sum) % self.p
            if reminder == 0:
                self.min_rem = min(self.min_rem, right_point-left_point+1)
                return
            if self.nums[left_point] > self.nums[right_point] and reminder >= self.nums[left_point]:
                current_sum += self.nums[left_point]
                left_point -= 1
            else:
                current_sum += self.nums[right_point]
                right_point += 1
        while left_point >= left:
            current_sum += self.nums[left_point]
            left_point -= 1
            if self.nums_sum - current_sum % self.p == 0:
                self.min_rem = min(self.min_rem, right_point-left_point+1)
                return
        while right_point <= right:
            current_sum += self.nums[right_point]
            right_point += 1
            if self.nums_sum - current_sum % self.p == 0:
                self.min_rem = min(self.min_rem, right_point-left_point+1)
                return
        return
        
    def divide_check(self, left, right):
        if left == right:
            if (self.nums_sum - self.nums[left]) % self.p == 0:
                if self.min_rem == -1:
                    self.min_rem = 1
                self.min_rem = min(self.min_rem, 1)
            return self.nums[left]
        if left > right:
            return 0
        mid = left + (right-left)//2
        l = self.divide_check(left, mid)
        r = self.divide_check(mid+1,right)
        if (self.nums_sum - (l+r)) % self.p == 0:
            self.min_rem = min(self.min_rem, right-left+1)
        self.cross_check(left, right, mid)
        return l+r
            
    def minSubarray(self, nums: List[int], p: int) -> int:
        self.nums_sum = sum(nums)
        self.p = p
        if self.nums_sum % self.p == 0:
            return 0
        self.nums = nums
        self.min_rem = len(nums) + 1
        self.divide_check(0, len(nums)-1)
        if self.min_rem >= len(nums):
            return -1
        return self.min_rem
