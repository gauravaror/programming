from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter()
        for i in nums:
            if i in counter:
                counter[i] += 1
            elif len(counter) < k:
                counter[i] = 1
            else:
                for j in counter:
                    counter[j] -= 1
                counter += Counter()
        return list(counter.keys())
