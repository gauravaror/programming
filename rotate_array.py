class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        if k == 0:
            return
        self.changes = 0
        def run_thing(a):
            first = True
            i = a
            prev = None
            while first or i != a:
                first = False
                prev,nums[i] = nums[i], prev
                self.changes += 1
                i = (i+k)%len(nums)
            nums[i] = prev
        #print(nums, len(nums)-(len(nums)/k + 1)*k%len(nums))
        for i in range(k):
            run_thing(i)
            if self.changes>=len(nums):
                break
        return nums
            
