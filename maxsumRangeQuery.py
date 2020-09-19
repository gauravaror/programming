class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        c = Counter()
        count_start = [0]*len(nums)
        count_end = [0]*len(nums)
        for i in requests:
            count_start[i[0]] += 1
            count_end[i[1]] += 1
        prev = 0
        count_final = [0]*len(nums)
        for i in range(len(nums)):
            prev += count_start[i]
            if i > 0:
                prev -= count_end[i-1]
            count_final[i] = prev
        print(count_final, count_start, count_end)
        nums.sort(reverse=True)
        count_final.sort(reverse=True)
        ind = 0
        output = 0
        for i,times in zip(nums,count_final):
            if times == 0:
                break
            output += i*times
            ind += 1
        return output % 1000000007
        
        
