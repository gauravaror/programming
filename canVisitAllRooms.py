class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        bit_rooms = [False]*len(rooms)
        bit_rooms[0] = True
        visited = 1
        queue = []
        queue.extend(rooms[0])
        while len(queue) > 0:
            item = queue.pop(0)
            if not bit_rooms[item]:
                queue.extend(rooms[item])
                bit_rooms[item] = True
                visited += 1
        return visited == len(rooms)
