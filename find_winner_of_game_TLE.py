from collections import Counter
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        c = Counter()
        hh = {}
        def ha(li):
            return ''.join([str(l) for l in li])
        if k >= len(arr)-1:
            return max(arr)
        while True:
            #print(arr)
            ca  = ha(arr)
            if ca in hh:
                oldc = hh[ca]
                newc = c.copy()
                newc -= oldc
                return newc.most_common()[0][0]
                    
            hh[ca] = c.copy()
            print(c)
            if arr[0] <= arr[1]:
                c[arr[1]] += 1
                if c[arr[1]] >= k:
                    return arr[1]
                elem = arr[0]
                del arr[0]
                arr.append(elem)
            else:
                c[arr[0]]+= 1
                if c[arr[0]] >= k:
                    return arr[0]
                elem = arr[1]
                del arr[1]
                arr.append(elem)
