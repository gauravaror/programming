def findLIS(s):
    length = len(s)
    dp = [1]*length
    for i in range(0,length):
        for j in range(i, length):
            if s[j] > s[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(dp)
    return max(dp)

assert findLIS([1,2,3,4,5,6]) == 6
assert findLIS([1,4,3]) == 2
assert findLIS([1,4,5,2,6]) == 4
assert findLIS([2,3,3,5]) == 3

