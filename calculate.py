class Solution:
    def calculate(self, s: str) -> int:
        stack =  []
        number = 0
        prev_num = 0
        prev_sign = True
        for i in s:
            #print(i, prev_sign, prev_num, number, stack)
            if i == '(':
                stack.append((number, prev_sign))
                prev_sign = True
                number = 0
            elif i.isdigit():
                prev_num = 10*prev_num + int(i)
            elif i in [ '+', '-']:
                if prev_sign:
                    number += prev_num
                else:
                    number -= prev_num
                prev_sign = True if i == '+' else False
                prev_num = 0
            elif i == ')':
                if prev_num > 0:
                    if prev_sign:
                        number += prev_num
                    else:
                        number -= prev_num
                    prev_num = 0
                    prev_sign = True
                num, sign = stack.pop()
                if sign:
                    number = num + number
                else:
                    number =  num - number
        if prev_sign:
            number += prev_num
        else:
            number -= prev_num
        return number
