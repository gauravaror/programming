from collections import Counter
import copy

def perfectSubstring(s, k):
    length = len(s)
    dp = [ [(False, Counter())]*length for _ in range(length)]
    for i in range(length):
        dp[i][i][1].update(s[i])
    total_seq = 0
    for i in range(length):
        for j in range(i+1, length):
            new_counter = copy.copy(dp[i][j-1][1])
            new_counter.update(s[j])
            all_same = True
            for t,v in new_counter.items():
                if not v == k:
                    all_same = False
                    break
            if all_same:
                total_seq+= 1
                dp[i][j] = (True, new_counter)
            else:
                dp[i][j] = (False, new_counter)
    return total_seq

perfectSubstring("dsdf", 1)
perfectSubstring("1102021222", 2)
perfectSubstring("1020122", 2)
perfectSubstring("1221221121", 3)
