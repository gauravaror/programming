class Solution:
    def decodeString(self, s: str) -> str:
        number = 0
        stack = []
        buffer = ""
        for i in s:
            if i.isnumeric():
                number = number*10 + int(i)
            elif i == '[':
                stack.append((buffer, number))
                number = 0
                buffer = ""
            elif i == ']':
                buf,rep = stack.pop()
                buffer = buf + buffer*rep
            else:
                buffer += i
            #print(buffer)
        return buffer
