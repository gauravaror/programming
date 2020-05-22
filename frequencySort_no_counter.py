from collections import Counter
from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = defaultdict(lambda: 0)
        for i in s:
            c[i] += 1
        hh = []
        for k,v in c.items():
            heapq.heappush(hh, (v,k))
        ans = ''
        print(hh)
        while(len(hh) > 0):
            item = heapq.heappop(hh)
            print(item)
            ans += item[1]*item[0]
        return ans[::-1]
