#  https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = False
        sum1 = 0
        first_space = True
        for i in str:
            if i in ['+', '-']:
                if first_space:
                    sign = i == '-'
                    first_space = False
                else:
                    break
            elif i.isdigit():
                sum1 = sum1*10 + (ord(i) - 48)
                if sum1 > 2147483647:
                    if sign:
                        return -2147483648
                    else:
                        return 2147483647
                first_space = False
            elif i == ' ':
                if not first_space:
                    break
            else:
                break
        if sign:
            sum1 = sum1*-1 
        return sum1
            
                
