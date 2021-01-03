class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prev = 0
        #rint(nums)
        for i in range(len(nums)):
            prev += nums[i]
            nums[i] = prev
        total = nums[-1]
        ans = 0
        #rint(nums)
        for idx,i in enumerate(nums):
            remaining = total-i
            each = remaining//2 + remaining%2
            if each < i:
                break
            index1 = bisect.bisect(nums, 2*i-1, lo=idx+1)
            index2 = bisect.bisect(nums, total-each, lo=index1)
            index2 = min(index2, len(nums)-1)
            print(remaining, i, each, 2*i, total-each, index1, index2)
            if index1 < index2:
                ans += (index2-index1)
        return ans % (10**9 + 7)
            
        
