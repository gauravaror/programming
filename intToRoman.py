class Solution:
    def intToRoman(self, num: int) -> str:
        a = {}
        a[1000] = 'M'
        a[900] = 'CM'
        a[500] = 'D'
        a[400] = 'CD'
        a[100] = 'C'
        a[90] = 'XC'
        a[50] = 'L'
        a[40] = 'XL'
        a[10] = 'X'
        a[9] = 'IX'
        a[5] = 'V'
        a[4] = 'IV'
        a[1] = 'I'
        order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        output = ''
        for i in order:
            while num >= i:
                num -= i
                output += a[i]
                if num <= 0:
                    break
        return output
