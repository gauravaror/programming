class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zero = 0
        first = 0
        while first  < len(binary)  and binary[first] == '1':
            first += 1
        for i in binary:
            if i == '0':
                zero += 1
        ones = len(binary) - zero - first
        if zero > 0:
            return '1'*(zero-1 + first) + '0' + '1'*ones
        else:
            return '1'*(first)
