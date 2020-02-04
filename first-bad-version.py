# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = (start+end)//2
        while start < end:
            if isBadVersion(mid):
                end = mid-1
            else:
                start = mid + 1
            mid = (start + end)//2
        if isBadVersion(start):
            return start
        else:
            return start + 1
        return start
        
