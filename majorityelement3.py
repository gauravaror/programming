class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el = []
        hh = Counter()
        for i in nums:
            hh[i] += 1
            found = False
            for ix,j in enumerate(el):
                if j[0] == i:
                    del el[ix]
                    el.append((j[0], j[1]+1))
                    found = True
                    break
            if not found:
                if len(el) < 3:
                    el.append((i,1))
                else:
                    el[0] = (el[0][0],el[0][1]-1)
                    el[1] = (el[1][0],el[1][1]-1)
                    el[2] = (el[2][0],el[2][1]-1)
                    if el[2][1] == 0:
                        del el[2]
                    if el[1][1] == 0:
                        del el[1]
                    if el[0][1] == 0:
                        del el[0]
                        
        output = []
        print(el)
        for i in el:
            if hh[i[0]] > len(nums)/3:
                output.append(i[0])
        return output
        
