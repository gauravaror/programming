class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        c = Counter()
        maxseq = [1]*len(nums)
        tracker = []
        for _ in nums:
            tracker.append(Counter())
        for i in range(len(nums)):
            c[1] += 1
            tracker[i][1] += 1
            for j in range(i):
                if nums[j] < nums[i]:
                    changed = True if maxseq[j] + 1 > maxseq[i] else False
                    maxseq[i] = max(maxseq[i], maxseq[j] + 1)
                    
                    if changed:
                        tracker[i][maxseq[i]] += tracker[j][maxseq[j]]
                        c[maxseq[i]] += tracker[j][maxseq[j]]
                    else:
                        tracker[i][maxseq[j] + 1] += tracker[j][maxseq[j]]
                        c[maxseq[j] + 1] += tracker[j][maxseq[j]]
            #print("Tracking tracker", tracker)
        #print(c, tracker)
        return c[max(c.keys())]
