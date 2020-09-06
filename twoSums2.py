class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map_num = {}
        for idx in range(len(numbers)):
            if target-numbers[idx] in map_num:
                return [map_num[target-numbers[idx]] +1 , idx+1]
            map_num[numbers[idx]] = idx
        return -1
            
        
