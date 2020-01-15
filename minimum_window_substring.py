from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_dic = Counter(t)
        w_start = 0
        w_end = 0
        str_len = len(s)
        min_length = {}
        
        currently_not_present = sum(freq_dic.values())
        while (w_start < str_len):
            print(w_start, w_end, freq_dic, currently_not_present)
            if (currently_not_present > 0):
                if (w_end >= str_len):
                    break
                if s[w_end] in freq_dic:
                    if (freq_dic[s[w_end]] > 0):
                        currently_not_present -= 1
                    freq_dic[s[w_end]] -= 1
                w_end += 1
            else:
                # move the window further to find minimum window   
                if s[w_start] in freq_dic:
                    print(s[w_start], freq_dic[s[w_start]])
                    if (freq_dic[s[w_start]] == 0):
                        # This is mimum window length register this and move ahead.
                        min_length[w_end - w_start + 1] = (w_start, w_end)
                        freq_dic[s[w_start]] += 1
                        w_start += 1
                        currently_not_present += 1
                    elif (freq_dic[s[w_start]] < 0):
                        freq_dic[s[w_start]] += 1
                        w_start += 1
                    else:
                        freq_dic[s[w_start]] += 1
                        #currently_not_present += 1
                else:
                    w_start += 1

        if len(min_length) == 0:
            return ""
        min_elem = min(min_length.items(), key=lambda x: x[0])
        print(min_length, min_elem)
        min_range = min_elem[1]
        return s[min_range[0]:min_range[1]]
                
                    
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("aaaaaaaaaaaabbbbbcdd","abcdd"))
