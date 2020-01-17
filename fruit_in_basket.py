from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        end = 0
        basket = defaultdict(int)
        basket[tree[end]] += 1
        collected_fruits = 1
        while (start < len(tree)):
            #print(basket)
            if (len(basket) <= 2):
                if end + 1 >= len(tree):
                    break
                end += 1
                basket[tree[end]] += 1
            else:
                basket[tree[start]] -= 1
                if basket[tree[start]] <= 0:
                    del basket[tree[start]]
                start += 1
            if (len(basket)) <= 2:
                cf = sum(basket.values())
                if cf > collected_fruits:
                    collected_fruits = cf
        return collected_fruits
