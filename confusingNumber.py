class Solution:
    def confusingNumber(self, N: int) -> bool:
        no_digit = True
        saved = N
        reverse_map = {0:0,1:1,6:9,8:8,9:6}
        digits = []
        while N > 0:
            if no_digit and N % 10 == 0:
                N = N/10
            else:
                no_digit = False
                num = int(N %10)
                if num not in reverse_map:
                    return False
                digits.append(reverse_map[num])
                N = N//10
        print(digits)
        ans = 0
        for i in digits:
            ans = ans*10 + i
        if ans != saved:
            return True
        else:
            return False
