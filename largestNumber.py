class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def get_digits(n):
            if n == 0:
                return [0]
            output = []
            while n > 0:
                a = n % 10
                inv = 100 if a == 0 else 1/a
                output.insert(0, a)
                n = n//10
            return output
        def comp(a, b):
            i = 0
            while i < len(a) and i < len(b):
                if a[i] == b[i]:
                    i += 1
                elif a[i] > b[i]:
                    return 1
                else:
                    return -1
            if len(a) == len(b):
                return 0
            if len(a) >= len(b):
                for k in range(i, len(a)):
                    gr = False
                    for j in range(0, len(b)):
                        if a[k] < b[j]:
                            return -1
                        if a[k] > b[j]:
                            gr = True
                    if gr:
                        return 1
                        
                return 1
            else:
                for k in range(i, len(b)):
                    gr = False
                    for j in range(0, len(a)):
                        if b[k] < a[j]:
                            return 1
                        if b[k] > a[j]:
                            gr=True
                    if gr:
                        return -1
                return -1
        digits = sorted(list(map(get_digits, nums)),  key=functools.cmp_to_key(comp), reverse=True)
        aa = 0
        print(digits)
        for i in range(len(digits)):
            for j in range(len(digits[i])):
                aa = aa*10 + digits[i][j]
        return str(aa)
