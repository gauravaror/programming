class Solution:
    def update(self, ind):
        self.tree[0] += 1
        while ind > 0:
            self.tree[ind] += 1
            ind -= (ind & -ind)
        
    def search(self, ind):
        output = 0
        if ind >= self.len_indexes:
            return output
        if ind == 0:
            return self.tree[0]
        while ind < self.len_indexes:
            output += self.tree[ind]
            ind += (ind&-ind)
        return output
    

    def reversePairs(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        self.len_indexes = len(nums_sorted)
        self.tree = [0]*self.len_indexes
        rev_pairs = 0
        for i in nums:
            ind_num = bisect.bisect_left(nums_sorted, 2*i+1)
            rev_pairs += self.search(ind_num)
            ind_num = bisect.bisect_left(nums_sorted, i)
            self.update(ind_num)
            #print(i, ind_num, rev_pairs, self.tree)
        return rev_pairs
