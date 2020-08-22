class Solution:
    def thousandSeparator(self, n: int) -> str:
        output = ""
        curr = 0
        if n == 0:
            return "0"
        while n > 0:
            d = n%10
            n = n//10
            output += str(d)
            curr += 1
            if curr == 3:
                curr = 0
                if n > 0:
                    output += '.'
        return output[::-1]
