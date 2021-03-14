class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = k
        ans = m = nums[k]
        while i >= 0 or j <= n-1:
            m = min(m, nums[i], nums[j])
            ans = max(ans, m*(j-i+1))
            if i <= 0 and j < n-1:
                j += 1
            elif j >= n-1 and i > 0:
                i -= 1
            elif i == 0 and j == n-1:
                i -= 1
                j += 1
            elif nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1
        return ans
