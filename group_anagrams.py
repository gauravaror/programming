import string
from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for i in strs:
            c = Counter()
            c.update(string.ascii_letters)
            c.update(i.lower())
            str_val =  ''.join([str(i) for i in list(c.values())])
            grouped_anagrams[str_val].append(i)
        return list(grouped_anagrams.values())
