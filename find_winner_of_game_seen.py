from collections import Counter
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        c = Counter()
        hh = {}
        def ha(li):
            return ''.join([str(l) for l in li])
        if k >= len(arr)-1:
            return max(arr)
        cont = 0 
        while True:                    
            if arr[0] <= arr[1]:
                elem = arr[0]
                del arr[0]
                arr.append(elem)
                cont = 1
            else:
                cont += 1
                elem = arr[1]
                del arr[1]
                arr.append(elem)
            if cont >= k:
                return arr[0]
