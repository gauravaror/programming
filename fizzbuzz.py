class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1,n+1):
            m3 = i%3 == 0
            m5 = i%5 == 0
            if m3 and m5:
                output.append('FizzBuzz')
            elif m3:
                output.append('Fizz')
            elif m5:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output

