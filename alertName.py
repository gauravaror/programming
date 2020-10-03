class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        nameTracker = defaultdict(lambda: [])
        def convertToInt(time):
            t = int(time[:2])*60 + int(time[3:])
            #print(time, t)
            return t
        output = set()
        for i,j in zip(keyName, keyTime):
            time = convertToInt(j)
            nameTracker[i].append(time)
        for k in nameTracker.keys():
            aa = sorted(nameTracker[k])
            for i in range(len(aa)-2):
                t1 = aa[i]
                t2 = aa[i+1]
                t3 = aa[i+2]
                if max(t1,t2,t3) - min(t1,t2,t3)<=60:
                    output.add(k)
                    break
        return sorted(list(output)) 
