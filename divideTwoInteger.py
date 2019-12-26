# https://leetcode.com/problems/divide-two-integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        final_sign = True
        if dividend < 0:
            final_sign = False
            dividend = dividend*-1
        if divisor < 0:
            final_sign = not final_sign
            divisor = divisor*-1
        
        quotiont = 0
        acdivisor = divisor
        times = 1
        while acdivisor > 0:
            if (dividend - divisor) <= 0:
                if (dividend - divisor) == 0:
                    quotiont += 1
                break
            elif dividend - acdivisor >= 0:
                dividend = dividend - acdivisor
                quotiont += times
                acdivisor = acdivisor + acdivisor
                times  = times + times                
            elif dividend - acdivisor < 0:
                acdivisor = acdivisor - (acdivisor >> 1)
                times  = times - (times >> 1)
          

        if not final_sign:
            if quotiont > 2147483647:
                return -2147483648
            quotiont = quotiont*-1
        if quotiont > 2147483647:
            quotiont = 2147483647
        return quotiont
            
        
        
        

