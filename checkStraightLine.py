class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def get_slope(c1, c2):
            if (c2[0] - c1[0]) == 0:
                return -1
            return (c2[1] - c1[1])/(c2[0] - c1[0])
        
        initial_slope = get_slope(coordinates[0], coordinates[1])
        for i in range(1, len(coordinates)-1):
            if initial_slope != get_slope(coordinates[i], coordinates[i+1]):
                return False
        return True
