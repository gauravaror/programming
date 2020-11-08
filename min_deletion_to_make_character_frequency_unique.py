class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter()
        c.update(s)
        hmap = defaultdict(int)
        for char,freq in c.items():
            hmap[freq] += 1
        print(hmap)
        delete = 0
        ks = list(hmap.keys())
        for fr in ks:
            count = hmap[fr]
            if count == 1:
                continue
            else:
                last_pos = fr-1
                for i in range(count-1):
                    while last_pos >=0 and hmap[last_pos] > 0:
                        last_pos -= 1
                    if last_pos < 0:
                        delete += fr
                    else:
                        hmap[last_pos] = 1
                        delete += fr-last_pos
        return delete
                        
                    
            
        
