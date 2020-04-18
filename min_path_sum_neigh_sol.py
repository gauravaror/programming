class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def get_hash(point):
            return str(point[0]) + '_' + str(point[1])
        def neigh(point):
            if point[1] < len(grid[0])-1:
                yield (point[0], point[1]+1)
            if point[0] < len(grid)-1:
                yield (point[0]+1, point[1])

        def find_min_path(point):
            if point == (len(grid)-1, len(grid[0])-1):
                return grid[point[0]][point[1]]
            mindis =  float('inf')
            for ne in neigh(point):
                if get_hash(ne) in dp:
                    this_dis = dp[get_hash(ne)]
                else:
                    this_dis = find_min_path(ne)
                mindis = min(mindis, this_dis)
            mindis +=  grid[point[0]][point[1]]
            if mindis != float(inf):
                dp[get_hash(point)] = mindis
            return mindis
        
        return find_min_path((0,0))
