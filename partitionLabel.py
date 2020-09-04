class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_indices = defaultdict(list)
        for idx,i in enumerate(S):
            char_indices[i].append(idx)
        print(char_indices)
        intervals = []
        for char, pos in char_indices.items():
            intervals.append([pos[0], pos[-1]])
        intervals.sort()
        print(intervals)
        curr_idx = 0
        start, end = intervals[0]
        last_end_time = 0
        output = []
        print()
        for c_st,c_end in intervals[1:]:
            if c_st > end:
                output.append(end+1 - last_end_time)
                last_end_time = end+1
                start, end = c_st, c_end
            else:
                end = max(end, c_end)
        output.append(len(S)-last_end_time)
        
        return output
