class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        multiplier = 1
        number = 0
        for i in digits[::-1]:
            number += multiplier*i
            multiplier *= 10
        #print(number)
        number += 1
        #print("2 ",number)
        output = []
        while number > 0:
            dig = number%10
            output.append(dig)
            number = number//10
            #print(number)
        return output[::-1]
