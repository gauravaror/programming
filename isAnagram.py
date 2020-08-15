class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0]*26
        t_freq = [0]*26
        for i in s:
            #print(ord(i) - 97)
            s_freq[ord(i) - 97] += 1
        for i in t:
            t_freq[ord(i)- 97] += 1
        for i in range(26):
            if not s_freq[i] == t_freq[i]:
                return False
        return True
