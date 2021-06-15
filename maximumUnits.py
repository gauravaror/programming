class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = 0
        units = 0
        
        #print(boxTypes)
        while i<len(boxTypes) and truckSize > 0:
            #print(i, truckSize, units,  boxTypes[i])
            if truckSize > boxTypes[i][0]:
                units += boxTypes[i][1]*boxTypes[i][0]
                truckSize -= boxTypes[i][0]
            else:
                units += boxTypes[i][1]*truckSize
                truckSize = 0
            i += 1
            #print('!', i, truckSize, units)
            
        return units

