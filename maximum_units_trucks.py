class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        idx = 0
        boxes = 0
        while truckSize > 0 and idx < len(boxTypes):
            if truckSize > boxTypes[idx][0]:
                truckSize -= boxTypes[idx][0]
                boxes += boxTypes[idx][0]*boxTypes[idx][1]
            else:
                boxes += boxTypes[idx][1]*truckSize
                truckSize = 0
            idx += 1
        return boxes
