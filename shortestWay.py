class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        si = len(source)
        ti = 0
        needed = 0
        all_chars = set(source)
        while ti < len(target):
            if si >= len(source):
                needed += 1
                si = 0
            if target[ti] not in all_chars:
                return -1
            if target[ti] != source[si]:
                si += 1
            else:
                si += 1
                ti += 1
        return needed
