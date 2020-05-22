from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter()
        c.update(s)
        o= ''
        for i in c.most_common():
            o += i[0]*i[1]
        return o
