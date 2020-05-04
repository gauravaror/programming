class Solution:
    def findComplement(self, num: int) -> int:
        rep = bin(num)[2:]
        output = 0
        for idx,i in enumerate(rep[::-1]):
            #print(idx, i)
            if i == '0':
                output += (1<<idx)
        return output
