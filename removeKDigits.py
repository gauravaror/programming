class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            prev_index = 0
            remove_index = 0
            for j in range(1, len(num)):
                if int(num[remove_index]) > int(num[j]):
                    break
                remove_index = j
            num = num[:remove_index] + num[remove_index+1:]
            #print(num)
        if len(num) == 0:
            return "0"
        return str(int(num))
