class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        map_items = defaultdict(list)
        for item in bank:
            for index in range(8):
                #print(item, index, map_items)
                intermediate = item[:index] + '*' + item[index+1:]
                map_items[intermediate].append(item)
        queue = [(start,0)]
        #print(map_items)
        while len(queue) > 0:
            item, pathlen = queue.pop(0)
            #print(item, end)
            if item == end:
                return pathlen
            for index in range(8):
                intermediate = item[:index] + '*' + item[index+1:]
                if intermediate in map_items:
                    for nex in map_items[intermediate]:
                        queue.append((nex, pathlen+1))
                    map_items[intermediate] = []
        return -1 
