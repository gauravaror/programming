from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = []
        if len(buildings) == 0:
            return []
        max_height = max(buildings, key=lambda x:x[2])[2]
        for building in buildings:
            heights.append([building[2], building[0], building[1]])
            heights.append([-building[2], building[1], building[0]])
        heights.sort(key=lambda x: [x[1], -x[0]])
        searchHeights = SortedList()
        outputs = []
        print(heights)
        for i in heights:
            height, coord_main, coord_sec = i
            if height > 0:
                searchHeights.add(height)
            else:
                searchHeights.remove(-height)
            current_max = searchHeights[-1] if len(searchHeights) > 0 else 0
            if len(outputs) != 0  and current_max == outputs[-1][1]:
                continue
            else:
                outputs.append([coord_main, current_max])
        return outputs
