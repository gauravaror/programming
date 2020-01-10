class Solution(object):
    
    def checkstring(self, first, second, rest_string):
        if len(rest_string) == 0:
            return True
        third = first + second
        third_str = str(third)
        if rest_string[:len(third_str)] == third_str:
            return self.checkstring(second, third, rest_string[len(third_str):])
        else:
            return False
        
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(1, len(num)):
            for j in range(1,len(num)):
                first = num[:i]
                second = num[i:i+j]
                if (first[0] == '0') and len(first) > 1:
                    continue
                if (second[0] == '0') and len(second) > 1:
                    continue
                first = int(first)
                second = int(second)
                rest_string = num[i+j:]
                print(first, second, rest_string)
                if len(rest_string) == 0:
                    continue
                if self.checkstring(first, second, rest_string):
                    return True
        return False
                
        
