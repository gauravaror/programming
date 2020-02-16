class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def binary_search(data):
            start = 0
            end = cols
            mid = (start + end)//2
            while start < end:
                if data[mid] < 0:
                    end = mid- 1
                else:
                    start = mid + 1
                mid = (start + end) // 2
            if data[start] < 0:
                start = start-1
            return start
            
        negatives = 0
        for i in range(rows):
            if (grid[i][-1] < 0):
                index = binary_search(grid[i])
                #negatives = cols*(rows-i-1)
                negatives += (cols-index-1)
                #break
        return negatives
