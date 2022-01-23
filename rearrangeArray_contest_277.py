class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = list(filter(lambda x:  x>0,  nums))
        neg = list(filter(lambda x:  x<0,  nums))
        output = []
        for i,j in zip(pos, neg):
            output.append(i)
            output.append(j)
        return output
