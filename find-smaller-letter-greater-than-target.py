class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)-1
        if (target < letters[start]):
            return letters[start]
        if (target > letters[end]):
            return letters[start]
        mid = (start + end) // 2
        while start < end:
            if (letters[mid] == target):
                if mid == len(letters)-1:
                    return letters[0]
                elif not letters[mid+1] == target:
                    return letters[mid+1]
                else:
                    start = mid + 1
            elif (letters[mid] < target):
                start = mid + 1
            else:
                end  = mid-1
            mid = (start + end )//2
        if (letters[start] <= target):
            if start == len(letters) -1:
                return letters[0]
            else:
                return letters[start+1]
        else:
            return letters[start]
