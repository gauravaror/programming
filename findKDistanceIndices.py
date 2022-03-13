class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        output = set()
        for idx, i in enumerate(nums):
            if i == key:
                for j in range(max(0, idx-k), min(len(nums)-1, idx+k)+1):   
                    output.add(j)
        return list(output)
                    
        
