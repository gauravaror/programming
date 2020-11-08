class Solution:
    def furthestBuilding(self, heights: List[int], bricks_: int, ladders_: int) -> int:
        self.max_index = 0
        @lru_cache(None)
        def backtrack(ci, bricks, ladders):
            if (ci >= len(heights) -1) or (bricks < (heights[ci+1] - heights[ci]) and ladders == 0):
                self.max_index = max(self.max_index, ci)
                return 
            if (heights[ci+1] - heights[ci]) <= 0:
                backtrack(ci+1, bricks, ladders)
            else:
                if (heights[ci+1] - heights[ci]) < bricks:
                    backtrack(ci+1, bricks- (heights[ci+1] - heights[ci]), ladders)
                if ladders > 0:
                    backtrack(ci+1, bricks, ladders-1)
        backtrack(0, bricks_, ladders_)
        return self.max_index
        
