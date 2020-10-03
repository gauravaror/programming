class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        nameTracker = defaultdict(lambda: [0]*1443)
        def convertToInt(time):
            t = int(time[:2])*60 + int(time[3:])
            #print(time, t)
            return t
        output = set()
        for i,j in zip(keyName, keyTime):
            time = convertToInt(j)
            nameTracker[i][time] =+  1
        for k in nameTracker.keys():
            isum = sum(nameTracker[k][:61])
            #print(k, nameTracker[k])
            if isum >= 3:
                output.add(k)
            else:
                for i in range(61,1440+1):
                    isum = isum + nameTracker[k][i] - nameTracker[k][i-61]
                    if isum >= 3:
                        output.add(k)
                        break
        return sorted(list(output))
        
