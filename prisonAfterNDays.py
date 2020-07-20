from collections import defaultdict
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        hm = {}
        def hash_c(cells):
            return ''.join([ str(c) for c in cells])
        def change_day(cells):
            #print("change day start", cells)
            newcells = [0]
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    newcells.append(1)
                else:
                    newcells.append(0)
            newcells.append(0)
            #print("change day ends", newcells)
            return newcells
        itera = N
        while (hash_c(cells) not in hm) and itera > 0:
            #print(hash_c(cells), itera)
            hm[hash_c(cells)] = itera
            itera -= 1
            cells = change_day(cells)
        if itera == 0:
            return cells
        else:
            #print("Repeated at", hm[hash_c(cells)], itera, N, hm[hash_c(cells)]-itera, hm)
            cycle = hm[hash_c(cells)] - itera
            cycle_start = hm[hash_c(cells)]
            leftitera = cycle_start % cycle
            for i in range(leftitera):
                cells = change_day(cells)
            return cells
