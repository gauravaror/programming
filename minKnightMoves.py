class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
        queue = deque()
        queue.append(((0,0),0))
        seen = set()
        seen.add((0,0))
        while len(queue) > 0:
            item,mov = queue.popleft()
            if item == (x,y):
                return mov
            for d in moves:
                nitem = (item[0] + d[0], item[1] + d[1])
                if nitem not in seen:
                    seen.add(nitem)
                    queue.append((nitem, mov+1))
