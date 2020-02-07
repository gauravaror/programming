def serverFile(rows, cols, grid):
    seen = {}
    this_iter = {}
    def adjacent(r, c):
        direction = [(-1,0), (0,-1), (0,1),  (1,0)]
        for i  in direction:
            if (r+i[0]) >=0 and (r + i[0]) < rows and (c + i[1]) >=0 and (c + i[1]) < cols:
                #print(r+i[0], c+i[1], rows, cols)
                yield (r+i[0], c+i[1])

    def dfs(r, c):
        this_iter[(r,c)] = 1
        #print("Starting", r,c, seen)
        if (r,c) in seen:
            return seen[(r,c)]
        current_min = float('inf')
        for col in adjacent(r,c):
            print("Columns ", col)
            if (col[0], col[1]) in this_iter:
                continue
            if (col[0], col[1]) in seen:
                this_distance = seen[(col[0], col[1])]
                if current_min > this_distance:
                    current_min = this_distance
            elif grid[col[0]][col[1]] == 0:
                this_distance =  1 + dfs(col[0], col[1])
                if current_min > this_distance:
                    current_min = this_distance
            else:
                seen[(r,c)] = 1
                return  1
            print(r, c, current_min)
        if current_min != float('inf'):
            seen[(r,c)] = current_min
        del this_iter[(r,c)]
        return current_min


    current_maximum = 0
    for i in range(rows):
        for j in range(cols):
            this_iter.clear()
            this_iter[(i,j)] = 1
            if (i,j) not in seen and grid[i][j] == 0:
                this_d = dfs(i, j)
                if this_d > current_maximum:
                    current_maximum = this_d
    print(seen)
    return max(seen.values())


print(serverFile(4,5, [[0,1,1,0,1],[0,1,0,1,0], [0,0,0,0,1], [0,1,0,0,0]]))
print(serverFile(5,5, [[1,0,0,0,0],[0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]))




