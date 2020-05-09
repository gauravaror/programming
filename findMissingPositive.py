class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def partition():
            q = 0 # Unusual place
            for i in range(len(nums)):
                if nums[i] > 0 and nums[q] <= 0:
                    temp = nums[q]
                    nums[q] = nums[i]
                    nums[i] = temp
                    while (q<i):
                        q += 1
                        if nums[q] <= 0:
                            break
                elif nums[i] <= 0 and nums[q] > 0:
                    q = i
            if nums[q] > 0:
                return len(nums)
            return q
        if len(nums) == 0:
            return 1
        k = partition()
        print(k, nums)
        for i in range(k):
            index = nums[i] if nums[i] > 0 else -nums[i]
            print(index)
            if index <= k:
                print(i, index, nums[index-1])
                if nums[index-1] > 0:
                    nums[index-1] = -nums[index-1]
                print(i, index, nums[index-1])
        print("fs", nums)
        for i in range(k):
            if nums[i] > 0:
                return i+1
        return k + 1
