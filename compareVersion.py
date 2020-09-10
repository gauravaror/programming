class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for a,b in itertools.zip_longest(v1, v2):
            if not a:
                a = '0'
            if not b:
                b = '0'
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0
