class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        jump=1
        bluething = 0
        for cp,i in enumerate(light,1):
            if i > cp and i > jump:
                jump = i
            else:
                if jump == cp:
                    #print(cp, jump)
                    bluething += 1
                    jump = cp+1
                
        return bluething
