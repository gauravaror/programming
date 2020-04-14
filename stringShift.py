class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        right = 0
        left = 0
        for i in shift:
            if i[0] == 0:
                left += i[1]
            else:
                right += i[1]
        direc = ""
        if right > left:
            direc = "right"
            amount = right- left
        else:
            direc = "left"
            amount  = left-right
        print(amount, left, right, direc)
        amount = amount % len(s)
        if direc == "right":
            return s[-amount:] + s[:-amount]
        else:
            return s[amount:] + s[:amount]
