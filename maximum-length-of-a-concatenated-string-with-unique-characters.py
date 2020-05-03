class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def get_rep(s):
            output = 0
            for i in s:
                output += 1 << ord(i) - ord('a')
            return output
        def get_sum(num):
            s = 0
            for i in bin(num)[2:]:
                s += int(i)
            return s
        newarr = []
        for i in arr:
            newarr.append(get_rep(i))
        dp = [0]
        for idx, i in enumerate(arr):
            if len(set(arr[idx])) - len(arr[idx]) != 0:
                continue
            for c in dp:
                if c&newarr[idx] == 0:
                    dp.append(c+newarr[idx])
        return max([get_sum(j) for j in dp])
