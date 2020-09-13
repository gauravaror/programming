class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        print(s_counter, t_counter, s_counter == t_counter)
        if s_counter != t_counter:
            return False
        s_idx = defaultdict(list)
        for idx,i in enumerate(s):
            s_idx[int(i)].append(idx)
        positions = [0]*10
        for i in t:
            i = int(i)
            if i not in s_idx:
                return False
            current_pos = s_idx[i][positions[i]]
            for j in range(i):
                if j in s_idx and len(s_idx[j]) > positions[j] and s_idx[j][positions[j]] < current_pos:
                    print("dsf", i, j, t, positions[j], current_pos)
                    return False
            positions[i] += 1
        return True
            
        
        
