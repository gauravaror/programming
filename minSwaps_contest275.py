class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total1 = sum(nums)
        firstn = sum(nums[-total1:])
        min_swaps = total1 - firstn
        curr_swaps = min_swaps
        for i in range(n, 2*n+1):
            current_position = (i)%n
            removed_position = (i -total1)%n
            #print(current_position, removed_position, total1, firstn, min_swaps)
            if nums[current_position] == 1:
                curr_swaps -= 1
            if nums[removed_position] == 1:
                curr_swaps += 1
            min_swaps = min(curr_swaps, min_swaps)
        return min_swaps
        
            
        
