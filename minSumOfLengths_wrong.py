class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum = 0
        dp = { 0: -1 }
        lens = []
        intervals = []
        for idx in range(len(arr)):
            cumsum += arr[idx]
            if cumsum-target in dp:
                le = idx-dp[cumsum-target]
                #lens.append(le)
                intervals.append([dp[cumsum-target], idx])
            dp[cumsum] = idx
        print(intervals)
        if len(intervals) < 2:
            return -1
        intervals = sorted(intervals)

        start, end = intervals[0]
        minlen = end-start
        for i in intervals[1:]:
            if i[0] < end:
                minlen = min(i[1]-i[0], minlen)
                end = max(i[1], end)
            else:
                lens.append(minlen)
                start,end = i
                minlen = end-start
        lens.append(minlen)
        print(lens)
        lens.sort()
        if len(lens) < 2:
            return -1
        else:
            return lens[0] + lens[1]
