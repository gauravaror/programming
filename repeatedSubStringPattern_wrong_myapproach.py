class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        starting = s[0]
        position_map = defaultdict(list)
        substring_map = defaultdict(list)
        current = s[0]
        starting_pos = 0
        first_substring = ""
        for i in range(1,len(s)):
            if s[i] == starting:
                position_map[starting_pos].append(current)
                substring_map[current].append(starting_pos)
                if not first_substring:
                    first_substring = current
                starting_pos = i
                current = s[i]
            else:
                current += s[i]
        position_map[starting_pos].append(current)
        substring_map[current].append(starting_pos)
        len_first_key = len(substring_map[first_substring])
        print(position_map, substring_map)
        if len(substring_map) == 1 and len_first_key > 1:
            return True
        if len_first_key <=1:
            return False
        for i in substring_map.keys():
            if i == first_substring:
                continue
            if len(substring_map[first_substring]) != len(substring_map[i]):
                return False
            first = None
            for i,j in zip(substring_map[first_substring], substring_map[i]):
                if first == None:
                    first = j-i
                else:
                    if first != (j-i):
                        return False
        return True
