class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        filnums = list(filter(lambda x: x >= 0, nums))
        if len(filnums) == 0:
            return 1
        mina = min(filnums)
        if mina > 1:
            return 1
        lena = max(nums) + 5
        normal = list(map(lambda x: x-mina, filnums))
        for i in range(len(normal)):
            idx = normal[i] % lena
            if idx < len(normal):
                if normal[idx] < lena:
                    normal[idx] = normal[idx] + lena
        print(normal)
        for i in range(len(normal)):
            if normal[i] < lena:
                return mina + i
        return mina + len(normal) 
