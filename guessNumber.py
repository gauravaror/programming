# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low < high:
            mid = (high+low) >> 1
            guess_output = guess(mid)
            if guess_output == 0:
                return mid
            if guess_output < 0:
                high = mid - 1
            else:
                low = mid + 1
        return low
 
